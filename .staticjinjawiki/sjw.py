#!/usr/bin/env python

# Static Jinja Wiki v1.0.1 - https://github.com/peterkaminski/staticjinjawiki

import os
from pathlib import Path
import re
import sys
import shutil

import argparse

# for exception
import jinja2

from markdown import Markdown
from mdx_wikilink_plus.mdx_wikilink_plus import WikiLinkPlusExtension

from staticjinja import Site

# Set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate HTML pages from Markdown wiki pages.')
    parser.add_argument('--dir', '-d', required=True, help='directory containing Markdown wiki pages')
    return parser

markdown_configs = {
    'mdx_wikilink_plus': {
        'base_url': '',
        'end_url': '.html',
        'url_whitespace': '_',
    },
}

markdown = Markdown(output_format="html5", extensions=[WikiLinkPlusExtension(markdown_configs['mdx_wikilink_plus'])])

def md_context(template):
    markdown_content = Path(template.filename).read_text()
    return {"post_content_html": markdown.convert(markdown_content)}

def render_md(site, template, **kwargs):
    # mangle the name the same way WikiLinkExtension does
    clean_name = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', template.name)
    out = site.outpath / Path(clean_name).with_suffix(".html")

    # compile and stream the result
    os.makedirs(out.parent, exist_ok=True)
    site.get_template(str(Path() / ".staticjinjawiki" / "page.html")).stream(**kwargs).dump(str(out), encoding="utf-8")

def main():
    argparser = init_argparse();
    args = argparser.parse_args();

    try:
        index_md_created = False
        if not os.path.exists(Path() / args.dir / "index.md"):
            shutil.copyfile(Path() / args.dir / "README.md", Path() / args.dir / "index.md")
            index_md_created = True

        # copy all the source files
        shutil.rmtree(Path() / args.dir / ".staticjinjawiki" / "output", ignore_errors=True)
        shutil.copytree(Path() / args.dir, Path() / args.dir / ".staticjinjawiki" / "output", ignore=shutil.ignore_patterns('.*'))
        shutil.copytree(Path() / args.dir / ".staticjinjawiki" / ".static", Path() / args.dir / ".staticjinjawiki" / "output" / ".static", ignore=shutil.ignore_patterns('.*'))

        site = Site.make_site(
            searchpath=args.dir,
            outpath=str(Path() / args.dir / ".staticjinjawiki" / "output"),
            contexts=[(r".*\.md", md_context)],
            rules=[(r".*\.md", render_md)],
        )
        site.render()

        if index_md_created:
            os.remove(Path() / args.dir / "index.md")

    except jinja2.exceptions.TemplateNotFound as err:
        sys.stderr.write("\nMissing template. Please create file: {}\n\n".format(err))
        sys.exit(1)

if __name__ == "__main__":
    exit(main())
