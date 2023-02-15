#!/usr/bin/env python

# Massive Wiki Builder v2.2.0 - https://github.com/peterkaminski/massivewikibuilder

# set up logging
import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# python libraries
import argparse
import datetime
import glob
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import traceback

# pip install
from dateutil.parser import parse # pip install python-dateutil
import jinja2
import yaml

from markdown import Markdown
sys.path.append('./mwb_wikilink_plus/')
from mwb_wikilink_plus.mwb_wikilink_plus import WikiLinkPlusExtension
from mwb_del.mwb_del import DelExtension

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate HTML pages from Markdown wiki pages.')
    parser.add_argument('--config', '-c', required=True, help='path to YAML config file')
    parser.add_argument('--output', '-o', required=True, help='directory for output')
    parser.add_argument('--templates', '-t', required=True, help='directory for HTML templates')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    parser.add_argument('--lunr', action='store_true', help='include this to create lunr index (requires npm and lunr to be installed, read docs)')
    parser.add_argument('--commits', action='store_true', help='include this to read Git commit messages and times, for All Pages')
    return parser

wikifiles = {}

def mwb_build_wikilink(path, base, end, url_whitespace, url_case):
    logging.debug("1 mwb_build_wikilink: path: %s", path)
    path_name = Path(path).name
    wikilink = Path(path_name).as_posix()  # use path_name if no wikipath
    if path_name in wikifiles.keys():
        wikipath = wikifiles[path_name]
        logging.debug("2 mwb_build_wikilink: wikipath: %s", wikipath)
        if wikipath.endswith('.md'):
            wikilink = Path(wikipath).with_suffix('.html').as_posix()
        else:
            wikilink = Path(wikipath).as_posix()
    logging.debug("3 mwb_build_wikilink return: %s", wikilink)
    return wikilink

# set up markdown
markdown_configs = {
    'mwb_wikilink_plus': {
        'base_url': '',
        'end_url': '.html',
        'url_whitespace': '_',
        'build_url': mwb_build_wikilink,
    },
}
markdown_extensions = [
    'footnotes',
    'tables',
    'fenced_code',
    WikiLinkPlusExtension(markdown_configs['mwb_wikilink_plus']),
    DelExtension(),
]
markdown = Markdown(output_format="html5", extensions=markdown_extensions)

# set up a Jinja2 environment
def jinja2_environment(path_to_templates):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path_to_templates)
    )

# load config file
def load_config(path):
    with open(path) as infile:
        return yaml.safe_load(infile)

# scrub wiki path to handle ' ', '_', '?', and '#' characters in wiki page names
# change ' ', ?', and '#' to '_', because they're inconvenient in URLs
def scrub_path(filepath):
    return re.sub(r'([ _?\#]+)', '_', filepath)

# index_wiki
def index_wiki(dir_wiki):

    logging.debug("index_wiki(): wiki folder %s: ", dir_wiki)

    mdfiles = [f for f in glob.glob(f"{dir_wiki}/**/*.md", recursive=True)] # TODO: consider adding .txt

    idx_data=[]
    posts=[]
    for i, f in enumerate(mdfiles):
        link = "/"+scrub_path(Path(f).relative_to(dir_wiki).with_suffix('.html').as_posix())
        title = Path(f).stem
        idx_data.append({"link":link, "title":title, "body": Path(f).read_text()})
        posts.append({"link":link, "title":title})

    logging.debug("index_wiki(): index length %s: ",len(idx_data))
    return idx_data, posts

# take a path object pointing to a Markdown file
# return Markdown (as string) and YAML front matter (as dict)
# for YAML, {} = no front matter, False = YAML syntax error
def read_markdown_and_front_matter(path):
    with path.open() as infile:
        lines = infile.readlines()
    # take care to look exactly for two `---` lines with valid YAML in between
    if lines and re.match(r'^---$',lines[0]):
        count = 0
        found_front_matter_end = False
        for line in lines[1:]:
            count += 1
            if re.match(r'^---$',line):
                found_front_matter_end = True
                break;
        if found_front_matter_end:
            try:
                front_matter = yaml.safe_load(''.join(lines[1:count]))
            except yaml.parser.ParserError:
                # return Markdown + False (YAML syntax error)
                return ''.join(lines), False
            # return Markdown + front_matter
            return ''.join(lines[count+1:]), front_matter
    # return Markdown + empty dict
    return ''.join(lines), {}

# read and convert Sidebar markdown to HTML
def sidebar_convert_markdown(path):
    if path.exists():
        markdown_text, front_matter = read_markdown_and_front_matter(path)
    else:
        markdown_text = ''
    return markdown.convert(markdown_text)

# handle datetime.date serialization for json.dumps()
def datetime_date_serializer(o):
    if isinstance(o, datetime.date):
        return o.isoformat()

def main():
    logging.debug("Initializing")

    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug("args: %s", args)

    # get configuration
    config = load_config(args.config)
    if not 'recent_changes_count' in config:
        config['recent_changes_count'] = 5

    # remember paths
    dir_output = os.path.abspath(args.output)
    dir_templates = os.path.abspath(args.templates)
    dir_wiki = os.path.abspath(args.wiki)

    # get a Jinja2 environment
    j = jinja2_environment(dir_templates)

    # set up lunr_index_filename and lunr_index_sitepath
    if (args.lunr):
        timestamp_thisrun = time.time()
        lunr_index_filename = f"lunr-index-{timestamp_thisrun}.js" # needed for next two variables
        lunr_index_filepath = Path(dir_output) / lunr_index_filename # local filesystem
        lunr_index_sitepath = '/'+lunr_index_filename # website
        lunr_posts_filename = f"lunr-posts-{timestamp_thisrun}.js" # needed for next two variables
        lunr_posts_filepath = Path(dir_output) / lunr_posts_filename # local filesystem
        lunr_posts_sitepath = '/'+lunr_posts_filename # website
    else:
        # needed to feed to themes
        lunr_index_sitepath = ''
        lunr_posts_sitepath = ''

    # render the wiki
    try:
        # remove existing output directory and recreate
        logging.debug("remove existing output directory and recreate")
        shutil.rmtree(dir_output, ignore_errors=True)
        os.mkdir(dir_output)

        # generate dict of filenames and their wikipaths
        for root,dirs,files in os.walk(dir_wiki):
            dirs[:]=[d for d in dirs if not d.startswith('.')]
            files=[f for f in files if not f.startswith('.')]
            readable_path = root[len(dir_wiki):]
            path = scrub_path(readable_path)
            for file in files:
                if file in ['netlify.toml']:
                    continue
                clean_name = scrub_path(file)
                if '.md' == Path(file).suffix.lower():
                    wikifiles[Path(file).stem] = f"{path}/{clean_name}"
                else:
                    wikifiles[Path(file).name] = f"{path}/{clean_name}"
        logging.debug("wikifiles: %s", wikifiles)
        # copy wiki to output; render .md files to HTML
        logging.debug("copy wiki to output; render .md files to HTML")
        all_pages = []
        page = j.get_template('page.html')
        build_time = datetime.datetime.now(datetime.timezone.utc).strftime("%A, %B %d, %Y at %H:%M UTC")
        if 'sidebar' in config:
            sidebar_body = sidebar_convert_markdown(Path(dir_wiki) / config['sidebar'])
        else:
            sidebar_body = ''
        for root, dirs, files in os.walk(dir_wiki):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [f for f in files if not f.startswith('.')]
            readable_path = root[len(dir_wiki)+1:]
            path = scrub_path(readable_path)
            if not os.path.exists(Path(dir_output) / path):
                os.mkdir(Path(dir_output) / path)
            logging.debug("processing %s", files)
            for file in files:
                logging.debug("main: processing: file: %s", file)
                if 'sidebar' in config and file == config['sidebar']:
                    continue
                clean_name = scrub_path(file)
                if file.lower().endswith('.md'):
                    # parse Markdown file
                    markdown_text, front_matter = read_markdown_and_front_matter(Path(root) / file)
                    if front_matter is False:
                        print(f"NOTE: YAML syntax error in front matter of '{Path(root) / file}'")
                        front_matter = {}
                    # output JSON of front matter
                    (Path(dir_output) / path / clean_name).with_suffix(".json").write_text(json.dumps(front_matter, indent=2, default=datetime_date_serializer))

                    # render and output HTML
                    markdown.reset() # needed for footnotes extension
                    markdown_body = markdown.convert(markdown_text)
                    html = page.render(
                        build_time=build_time,
                        wiki_title=config['wiki_title'],
                        author=config['author'],
                        repo=config['repo'],
                        license=config['license'],
                        title=file[:-3],
                        markdown_body=markdown_body,
                        sidebar_body=sidebar_body,
                        lunr_index_sitepath=lunr_index_sitepath,
                        lunr_posts_sitepath=lunr_posts_sitepath,
                    )
                    (Path(dir_output) / path / clean_name).with_suffix(".html").write_text(html)

                    # get commit message and time
                    if args.commits:
                        p = subprocess.run(["git", "-C", Path(root), "log", "-1", '--pretty="%cI\t%an\t%s"', file], capture_output=True, check=True)
                        (date,author,change)=p.stdout.decode('utf-8')[1:-2].split('\t',2)
                        date = parse(date).astimezone(datetime.timezone.utc).strftime("%Y-%m-%d, %H:%M")
                    else:
                        date = ''
                        change = ''
                        author = ''

                    # remember this page for All Pages
                    all_pages.append({
                        'title':f"{readable_path}/{file[:-3]}".lstrip('/'),
                        'path':f"{path}/{clean_name[:-3]}.html",
                        'date':date,
                        'change':change,
                        'author':author,
                    })
                # copy all original files
                logging.debug("copy all original files")
                shutil.copy(Path(root) / file, Path(dir_output) / path / clean_name)

        # build Lunr search index if --lunr
        if (args.lunr):
            logging.debug("building lunr index: %s", lunr_index_filepath)
            # ref: https://lunrjs.com/guides/index_prebuilding.html
            pages_index, posts = index_wiki(dir_wiki)
            pages_index_bytes = json.dumps(pages_index).encode('utf-8') # NOTE: build-index.js requires text as input - convert dict to string (then do encoding to bytes either here or set `encoding` in subprocess.run())
            with open(lunr_index_filepath, "w") as outfile:
                print("lunr_index=", end="", file=outfile)
                outfile.seek(0, 2) # seek to EOF
                p = subprocess.run(['node', 'build-index.js'], input=pages_index_bytes, stdout=outfile, check=True)
            with open(lunr_posts_filepath, "w") as outfile:
                print("lunr_posts=", posts, file=outfile)

        # and then the search javascript will do this:
        #   <script src="/lunr-index-1656192217.474129.js"></script>
        #   <script src="/lunr-posts-1656192217.474129.js"></script>
        # and the variables `lunr_index` will contain the index, `lunr_posts` will contain the links+titles

        # temporary handling of search.html - TODO, do this better :-)
        search_page = j.get_template('search.html')
        html = search_page.render(
            build_time=build_time,
            wiki_title=config['wiki_title'],
            author=config['author'],
            repo=config['repo'],
            license=config['license'],
            sidebar_body=sidebar_body,
            lunr_index_sitepath=lunr_index_sitepath,
            lunr_posts_sitepath=lunr_posts_sitepath,
        )
        (Path(dir_output) / "search.html").write_text(html)

        # copy README.html to index.html if no index.html
        logging.debug("copy README.html to index.html if no index.html")
        if not os.path.exists(Path(dir_output) / 'index.html'):
            shutil.copyfile(Path(dir_output) / 'README.html', Path(dir_output) / 'index.html')

        # copy static assets directory
        logging.debug("copy static assets directory")
        if os.path.exists(Path(dir_templates) / 'mwb-static'):
            logging.warning("mwb-static is deprecated. please use 'static', and put mwb-static inside static - see docs")
            shutil.copytree(Path(dir_templates) / 'mwb-static', Path(dir_output) / 'mwb-static')
        if os.path.exists(Path(dir_templates) / 'static'):
            shutil.copytree(Path(dir_templates) / 'static', Path(dir_output), dirs_exist_ok=True)

        # build all-pages.html
        logging.debug("build all-pages.html")
        if args.commits:
            all_pages_chrono = sorted(all_pages, key=lambda i: i['date'], reverse=True)
        else:
            all_pages_chrono = ''
        all_pages = sorted(all_pages, key=lambda i: i['title'].lower())
        html = j.get_template('all-pages.html').render(
            build_time=build_time,
            pages=all_pages,
            pages_chrono=all_pages_chrono,
            wiki_title=config['wiki_title'],
            author=config['author'],
            repo=config['repo'],
            license=config['license'],
            lunr_index_sitepath=lunr_index_sitepath,
            lunr_posts_sitepath=lunr_posts_sitepath,
        )
        (Path(dir_output) / "all-pages.html").write_text(html)

        # build recent-pages.html
        logging.debug("build recent-pages.html")
        recent_pages = all_pages_chrono[:config['recent_changes_count']]
        html = j.get_template('recent-pages.html').render(
            build_time=build_time,
            pages=recent_pages,
            wiki_title=config['wiki_title'],
            author=config['author'],
            repo=config['repo'],
            license=config['license'],
            sidebar_body=sidebar_body,
            lunr_index_sitepath=lunr_index_sitepath,
            lunr_posts_sitepath=lunr_posts_sitepath,
        )
        (Path(dir_output) / "recent-pages.html").write_text(html)

        # done
        logging.debug("done")

    except subprocess.CalledProcessError as e:
        print(f"\nERROR: '{e.cmd[0]}' returned error code {e.returncode}.")
        print(f"Output was '{e.output}'")
        if e.cmd[0] == 'node':
            print(f"\nYou may need to install Node modules with 'npm ci'.\n")
        if e.cmd[0] == 'git':
            print(f"\nThere was a problem with Git.\n")
    except jinja2.exceptions.TemplateNotFound as e:
        print(f"\nCan't find template '{e}'.\n\nTheme or files in theme appear to be missing, or theme argument set incorrectly.\n")
    except FileNotFoundError as e:
        print(f"\n{e}\n\nCheck that arguments specify valid files and directories.\n")
    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())
