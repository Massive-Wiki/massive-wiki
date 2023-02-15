# Massive Wiki Builder

Massive Wiki Builder is a static site generator for turning [Massive Wikis](https://massive.wiki/) into static HTML websites.

## Typical Hierarchy

Typically, there is a `.massivewikibuilder` directory, which contains `massivewikibuilder` (this repo), and other related files and directories.

The `.` character is important when the MWB workspace directory is within the wiki itself.  MWB ignores dotfiles and dot-directories, so as it builds, it will ignore anything inside (for instance) `.obsidian` or `.massivewikibuilder` directories.  If you don't have it set up this way, MWB will continue to try to copy and convert the files in the output directory, and it will start an infinite loop, which will stop when the directory names get too long.

```
--/ # root of wiki directories
---- .massivewikibuilder/ # MWB workspace
------ mwb.yaml # config for this wiki
------ massivewikibuilder/ # MWB
------ massive-wiki-themes/ # off-the-shelf themes, not customized
-------- alto/ # a specific theme, customized for this wiki
------ this-wiki-themes/ # theme(s) used for this wiki
-------- alto/ # a specific theme, customized for this wiki
------ output/ # MWB writes .html, .md, and .json files here
```

Note that MWB removes (if necessary) and recreates the `output` directory each time it is run.

## Static Files

Note: Prior to v1.9.0, MWB handled static files slightly differently. If `mwb-static` existed, it copied it from the theme directory to the output directory. Starting with v1.9.0, it will still do this, but it will output a warning, `WARNING:root:WARNING:root:mwb-static is deprecated, please use 'static'`. The warning is meant to suggest that you should move `mwb-static` into the `static` directory at the top level of the theme.  `static` is described below.

After the HTML pages are built from the Markdown files, if a directory named `static` exists at the top level of the theme, all the files and directories within it are copied to the root of the output directory.  By convention, static files such as CSS, JavaScript, and images are put in a directory inside `static` called `mwb-static`. Favicon files and other files that should be at the root of the website are put at the root of `static`.

The name `static` is used in the theme because it's descriptive, and won't collide with anything in the wiki. (The _content_ of `static` is copied, but not `static` itself.)

The `mwb-static` convention is used to contain static files used by the wiki, and instead of `static`, it is named `mwb-static` so it is less likely to collide with a wiki directory with the same name. (In contrast to `static` in the theme, `mwb-static` itself _is_ copied to the output directory, where all the wiki files and directories live.)

In the theme:

```
--/ # root of theme
---- static/ # anything in here is copied to the root of the output
------ favicon.ico # for instance, favicon.ico
------ mwb-static/ # static files and subdirectories that don't need to be at the root of the website
-------- css/
-------- js/
-------- images/
```

Results in the output website:

```
--/ # root of website
--- favicon.ico # for instance, favicon.ico
---- mwb-static/ # static files and subdirectories that don't need to be at the root of the website
------ css/
------ js/
------ images/
```

Side note about favicon files; it is suggested to use a favicon generator such as [RealFaviconGenerator](https://realfavicongenerator.net/) to create the various icon files needed for different platforms. This note is meant for informational purposes, and does not represent an endorsement of RealFaviconGenerator in particular.

## Install

(not yet completed)
(remember to `pip install -r requirements.txt`)

(clone massive-wiki-themes repo, call it massive-wiki-themes)

## Build

In `.massivewikibuilder/`:

```shell
./mwb.py -c mwb.yaml -w .. -o output -t massive-wiki-themes/alto
```

If you want to print a log what's happening during the build, set the `LOGLEVEL` environment variable to `DEBUG`.

On the command line, do:

```shell
LOGLEVEL=DEBUG ./mwb.py -c mwb.yaml -w .. -o output -t massive-wiki-themes/alto
```

or:

```shell
export LOGLEVEL=DEBUG
./mwb.py -c mwb.yaml -w .. -o output -t massive-wiki-themes/alto
```

In `netlify.toml`, do:

```toml
[build.environment]
  LOGLEVEL = "DEBUG"
```

## Git Commits

To output authors, commit messages, and timestamps for each page in the All Pages page, include the `--commits` flag:

```shell
./mwb.py -c mwb.yaml -w .. -o output -t massive-wiki-themes/alto --commits
```

In the `all-pages.html` template (template may have a different file name), the following variables are available when `--commits` is active:

- `pages_chrono` - an array of all the pages, sorted chronologically
- `page.author` - the author name of the most recent commit for this page
- `page.change` - the commit message for the most recent commit for this page
- `page.date` - the timestamp for the most recent commit for this page

If `--commits` is not active, each of those variables is set to empty string `''`.

## Lunr

To build an index for the [Lunr](https://lunrjs.com/) search engine, include the `--lunr` flag:

```shell
./mwb.py -c mwb.yaml -w .. -o output -t massive-wiki-themes/alto --lunr
```

Lunr is a JavaScript library, so Node.js (`node`) and the Lunr library must be installed.

To install Node, see <https://nodejs.org/en/download/>. On Mac, you may want to do `brew install node`.

To install Lunr, in `.massivewikibuilder/massivewikibuilder` do:

```shell
npm ci # reads package.json and package-lock.json
```

When MWB runs, the Lunr indexes are generated at the root of the output directory, named like this (numbers change every microsecond): `lunr-index-1656193058.85086.js` (the reverse index) and `lunr-posts-1656193058.85086.js` (relates filepaths used by Lunr as keys, to human-readable page names).

Two template variables, `lunr_index_sitepath` and  `lunr_posts_sitepath`, containing the website paths to the generated index JavaScript files, are passed to templates as the pages are built.

In templates, loading the indexes is done like this:

```
{% if lunr_index_sitepath != '' %}
<script src="{{lunr_index_sitepath}}"></script>
{% endif %}
{% if lunr_posts_sitepath != '' %}
<script src="{{lunr_posts_sitepath}}"></script>
{% endif %}
```

which results in this on the generated webpage:

```html
<script src="/lunr-index-1656193058.85086.js"></script>
<script src="/lunr-posts-1656193058.85086.js"></script>
```

Add the rest of the code to the `<script>` sections of your pages to enable Lunr:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js"></script>
<script>var index = lunr.Index.load(lunr_index)</script>
// ...
const searchResultList = index.search(searchString).map((item) => {
              return lunr_posts.find((post) => item.ref === post.link)
          })
// ...
```



## Deploy (Netlify)

For Netlify deploys, you can include a `netlify.toml` file like this at the root of your repo:

```toml
[build]
  ignore = "/bin/false"
  base = ".massivewikibuilder"
  publish = "output"
  command = "./mwb.py -c mwb.yaml -w ../.. -o ../output -t ../massive-wiki-themes/alto"

[build.environment]
  PYTHON_VERSION = "3.8"
```

It is recommended that you make a copy of `massive-wiki-themes` called `this-wiki-themes` at the same directory level, then customize your themes inside of `this-wiki-themes`.

The build command would then be (substitute your theme name instead of `alto` as necessary:

```shell
./mwb.py -c mwb.yaml -w ../.. -o ../output -t ../this-wiki-themes/alto
```

 

## Develop

Because static assets have an absolute path, you may want to start a local web server while you're developing and testing.  Change to the output directory and run this command:

```
python3 -m http.server
```

## Themes

MWB uses a simple theming system.  All the files for one theme are placed in a subdirectory in the themes directory, usually `massive-wiki-themes`.  For example, the Alto theme is in `massive-wiki-themes/alto`, and to use the Alto theme, pass `-t massive-wiki-themes/alto` to MWB.

MWB builds the pages with Jinja2, so you can use Jinja2 directives within the HTML files to include wiki metadata and wiki content.  You can also use the Jinja2 `include` functionality to extract reused parts of the page to HTML "partial" files.

Themes are in a separate repo, [github/peterkaminski/massive-wiki-themes](https://github.com/peterkaminski/massive-wiki-themes). For Massive Wiki Builder v2.2.0, you should use Massive Wiki Themes version 2023-02-09-001 or later.