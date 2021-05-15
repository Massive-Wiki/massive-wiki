# Massive Wiki Themes

Massive Wiki Builder and Missive Weaver use a simple theming system.  All the files for one theme are placed in a subdirectory in the themes directory, usually `massive-wiki-themes`.  For example, the Alto theme is in `massive-wiki-themes/alto`, and to use the Alto theme, pass `-t massive-wiki-themes/alto` to MWB.

The apps build the pages with Jinja2, so you can use Jinja2 directives within the HTML files to include wiki metadata and wiki content.  You can also use the Jinja2 `include` functionality to extract reused parts of the page to HTML "partial" files.

These themes are included in this repo:

- Alto - a simple but nice responsive theme, implemented with [Bulma](https://bulma.io).  It would be fairly easy to add more Bulma components to the pages.
- Skeleton - a straightforward, plain HTML theme, demonstrating a minimally viable theme.  It uses `include` functionality for a navbar and footer.
- Super Skeleton - the bare minimum, even more minimal than Skeleton; not even includes.
