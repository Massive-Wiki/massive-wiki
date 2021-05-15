# Massive Wiki Builder

Massive Wiki Builder is a static site generator for turning [Massive Wikis](https://massive.wiki/) into static HTML websites.

Typically, it is installed at the root of the wiki, next to all the top-level Markdown files, in a subdirectory named `.massivewikibuilder`.

The `.` character is important when the MWB directory is within the wiki itself.  MWB ignores dotfiles and dot-directories, so as it builds, it will ignore anything inside (for instance) `.obsidian` or `.massivewikibuilder` directories.  If you don't have it set up this way, MWB will continue to try to copy and convert the files in the output directory, and it will start an infinite loop, which will stop when the directory names get too long.

## Typical Hierarchy

```
--/ # root of wiki directories
---- .massivewikibuilder/ # MWB and its input/output
------ output/ # MWB writes .html, .md, and .json files here
------ themes/ # all the themes
-------- alto/ # a specific theme
```

Note that MWB removes (if necessary) and recreates the `output` directory each time it is run.

## Install

(not yet completed)
(remember to `pip install -r requirements.txt`)

(clone massive-wiki-themes repo, call it massive-wiki-themes)

## Build

In `.massivewikibuilder/`:

```
./mwb.py -c mwb.yaml -w .. -o output -t massive-wiki-themes/alto
```

## Develop

Because static assets have an absolute path, you may want to start a local web server while you're developing and testing.  Change to the output directory and run this command:

```
python3 -m http.server
```

## Themes

MWB uses a simple theming system.  All the files for one theme are placed in a subdirectory in the themes directory, usually `massive-wiki-themes`.  For example, the Alto theme is in `massive-wiki-themes/alto`, and to use the Alto theme, pass `-t massive-wiki-themes/alto` to MWB.

MWB builds the pages with Jinja2, so you can use Jinja2 directives within the HTML files to include wiki metadata and wiki content.  You can also use the Jinja2 `include` functionality to extract reused parts of the page to HTML "partial" files.

Themes are in a separate repo, [github/peterkaminski/massive-wiki-themes](https://github.com/peterkaminski/massive-wiki-themes).

