# Massive Wiki Themes

Version 2023-02-09-001.

Massive Wiki Builder and Missive Weaver use a simple theming system.  All the files for one theme are placed in a subdirectory in the themes directory, usually `massive-wiki-themes`.  For example, the Alto theme is in `massive-wiki-themes/alto`, and to use the Alto theme, pass `-t massive-wiki-themes/alto` to MWB.

The apps build the pages with Jinja2, so you can use Jinja2 directives within the HTML files to include wiki metadata and wiki content.  You can also use the Jinja2 `include` functionality to extract reused parts of the page to HTML "partial" files.

See the Massive Wiki Builder repo for more information on running MWB: <https://github.com/peterkaminski/massivewikibuilder/>

These themes are included in this repo:

- Alto - a simple but nice responsive theme, implemented with [Bulma](https://bulma.io).  It would be fairly easy to add more Bulma components to the pages.
- Basso - like Alto, but with a simple Sidebar on the left, and support for search
- Skeleton - a straightforward, plain HTML theme, demonstrating a minimally viable theme.  It uses `include` functionality for a navbar and footer.
- Super Skeleton - the bare minimum, even more minimal than Skeleton; not even includes.

## Typical Hierarchy

Typically, there is a `.massivewikibuilder` directory, which contains `massivewikibuilder` and `massive-wiki-themes` (this repo), and other related files and directories.

It is recommended that you make a copy of `massive-wiki-themes` called `this-wiki-themes` at the same directory level, then customize your themes inside of `this-wiki-themes`.  See the Massive Wiki Builder README for details of specifying your theme directory.

The `.` character is important when the MWB workspace directory is within the wiki itself.  MWB ignores dotfiles and dot-directories, so as it builds, it will ignore anything inside (for instance) `.obsidian` or `.massivewikibuilder` directories.  If you don't have it set up this way, MWB will continue to try to copy and convert the files in the output directory, and it will start an infinite loop, which will stop when the directory names get too long.

```
--/ # root of wiki directories
---- .massivewikibuilder/ # MWB workspace
------ mwb.yaml # config for this wiki
------ massivewikibuilder/ # MWB
------ massive-wiki-themes/ # off-the-shelf themes, not customized
-------- alto/ # a specific theme, not customized
------ this-wiki-themes/ # theme(s) used for this wiki
-------- alto/ # a specific theme, customized for this wiki
------ output/ # MWB writes .html, .md, and .json files here
```

Note that MWB removes (if necessary) and recreates the `output` directory each time it is run.

## Static Files

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

