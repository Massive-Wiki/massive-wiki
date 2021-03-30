# Ideas and Concerns

This page collects various various thoughts, connections, and reflections about Massive Wiki.  It is ever-changing.

## Page Contention

Within one multiplayer MaSVF installation, how does an editing tool interact with the syndication / synchronization process, particularly when multiple people are editing?

For synchronization-by-git, does there need to be some real-time synchronization (XMPP? other?) happening as well?

Is there a role for git branches?

When/how do we deploy CRDT (or OT or similar) for MaSVF?

## Decentralization and Syndication

Each MaSVF installation uses its own file sharing and versioning solution, including git repo, Nextcloud file sharing, etc.

What support does MaSVF provide for sharing *between* installations? When is page history preserved, and when is it discarded? How do forks and merges work?

## Markdown Flavors

MaSVF will need to figure out how to support various flavors and levels of Markdown.

## Semantic Meaning of Header Levels

Life will be better if we sort of standardize how to use the H1, H2, H3, etc. header levels.

Case in point: is there always an H1 at the top of the page with the page title?  Or is H1 used throughout the page as the top-level semantic separator?

## Website "Furniture"

(By analogy with [street furniture](https://en.wikipedia.org/wiki/Street_furniture).)

- Navbar / sidebar
- Recent Changes / All Files
- Breadcrumbs
- Pagination of Lists
- Search

## Metadata

- tags / categories
- date and authorship
- globally-unique identifiers for pages and other elements

## Link Syntax

MaSVF uses double square brackets for links internal to the wiki, but there are subtle concerns about the syntax.

- intra-page anchors / headers
- converting page names with non-URL-safe characters to URLs in a way that's deterministic and compatible across the MaSVF ecosystem
- rewriting links when page names change

