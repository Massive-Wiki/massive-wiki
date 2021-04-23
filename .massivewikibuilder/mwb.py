#!/usr/bin/env python

# Massive Wiki Builder v1.0.0 - https://github.com/peterkaminski/massivewikibuilder

import argparse
import os
import re
import shutil
import sys

from pathlib import Path

import jinja2

from markdown import Markdown
from mdx_wikilink_plus.mdx_wikilink_plus import WikiLinkPlusExtension

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate HTML pages from Markdown wiki pages.')
    parser.add_argument('--output', '-o', required=True, help='directory for output')
    parser.add_argument('--templates', '-t', required=True, help='directory for HTML templates')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser

# set up markdown
markdown_configs = {
    'mdx_wikilink_plus': {
        'base_url': '',
        'end_url': '.html',
        'url_whitespace': '_',
    },
}
markdown = Markdown(output_format="html5", extensions=[WikiLinkPlusExtension(markdown_configs['mdx_wikilink_plus'])])

# set up a Jinja2 environment
def jinja2_environment(path_to_templates):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path_to_templates)
    )

def main():
    argparser = init_argparse();
    args = argparser.parse_args();

    # remember paths
    dir_output = os.path.abspath(args.output)
    dir_templates = os.path.abspath(args.templates)
    dir_wiki = os.path.abspath(args.wiki)

    # get a Jinja2 environment
    j = jinja2_environment(dir_templates)

    # render the wiki
    try:
        # remove existing output directory and recreate
        shutil.rmtree(dir_output, ignore_errors=True)
        os.mkdir(dir_output)

        # copy wiki to output; render .md files to HTML
        page = j.get_template('page.html')
        for root, dirs, files in os.walk(dir_wiki):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [f for f in files if not f.startswith('.')]
            path = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', root[len(dir_wiki)+1:])
            if not os.path.exists(Path(dir_output) / path):
                os.mkdir(Path(dir_output) / path)
            for file in files:
                clean_name = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', file)
                if file.lower().endswith('.md'):
                    markdown_body = markdown.convert((Path(root) / file).read_text())
                    html = page.render(markdown_body=markdown_body)
                    (Path(dir_output) / path / clean_name).with_suffix(".html").write_text(html)
                shutil.copy(Path(root) / file, Path(dir_output) / path / clean_name)
        if not os.path.exists(Path(dir_output) / 'index.html'):
            shutil.copyfile(Path(dir_output) / 'README.html', Path(dir_output) / 'index.html')
        if os.path.exists(Path(dir_templates) / 'mwb-static'):
            shutil.copytree(Path(dir_templates) / 'mwb-static', Path(dir_output) / 'mwb-static')
        

    except Exception as e:
        print(e)

if __name__ == "__main__":
    exit(main())
