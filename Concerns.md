# Markdown Flavors

MaSVF will need to figure out how to support various flavors and levels of Markdown.

# Metadata

- tags / categories
- date and authorship
- globally-unique identifiers for pages and other elements

# Link Syntax

MaSVF uses double square brackets for links internal to the wiki, but there are subtle concerns about the syntax.

- intra-page anchors / headers
- converting page names with non-URL-safe characters to URLs in a way that's deterministic and compatible across the MaSVF ecosystem
- rewriting links when page names change

# Decentralization and Syndication

Each MaSVF installation uses its own file sharing and versioning solution, including git repo, Nextcloud file sharing, etc.

What support does MaSVF provide for sharing *between* installations? When is page history preserved, and when is it discarded? How do forks and merges work?