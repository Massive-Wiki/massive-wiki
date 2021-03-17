#!/usr/bin/env python3

import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

with open("readme.md", "r", encoding="utf-8") as input_file:
    md = input_file.read()
html = markdown.markdown(md, extensions=[WikiLinkExtension(base_url='/', end_url='.html')])

with open("readme.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(html)
