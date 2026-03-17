# The Massive Wiki Pattern  

### The Massive Wiki pattern versus the MediaWiki pattern

The Massive Wiki pattern <https://massive.wiki/> is more flexible and less structured than the MediaWiki pattern. As a result, you have more control (and thence, more responsibility) over how you edit the wiki and make your content and edits available to the world.

In the MediaWiki world, a wiki is a set of text files, stored in a database on a server, with software that supports editing and viewing the files on a website.

In the Massive Wiki world, a wiki is a set of text files, stored on your computer, on other people's computers, and, optionally, stored in a "git forge" (a database hub, such as GitHub), and optionally, published on a website. There are many editing, viewing, and collaborating patterns that are then enabled by this layout, including:

- The publisher edits; the public views as a website; no collaboration.
- The publisher edits; anyone can download a single file or all the files, anyone can edit their copy and submit it back to the publisher.
- A small team collaborates on the text files using peer-to-peer file synchronization software, such as `syncthing`, or shared drives. The wiki may or may not be published to others.
- There are multiple publishers, each with possibly different edits. TODO: maybe say more?
- Borrowing a very well-known pattern from the software development world, the wiki is published (on a Git forge), and anyone can edit using the Git/GitHub "fork and pull" / "pull request" model, and submit their changes back to the publisher. They can also just publish and maintain their fork. Good news: this model is superlative for geeks. Bad news: this model only works for geeks.
- This is happening in 2026: Normal people will be able to collaborate on Massive Wikis using agentic AI (like Claude Code), working with the AI in plain language and concepts, and having the AI manage the technical processes.
- To make collaboration easier, sometimes the publisher of a wiki will grant read/write access to the central repository to certain people they trust. This uses the git forge as the authentication / coordination point, which requires one-time technical setup, and using a git-aware tool such as Obsidian to synchronize changes. Again, in 2026 this will get easier and better with agentic AI.

In any of these models, the publisher might be a single person, or a team of people acting as a single entity. The publisher takes responsibility to ensure the wiki is published, and for managing collaboration and publishing updates. If the publisher is unable or unwilling to maintain the publication, it may get stale or disappear. Pro tip: Showing gratitude to the publishers in your community helps them keep publishing.

Separately from the technical process of editing and publishing, there are legal and ethical issues of copyright and intellectual property.

In the MediaWiki world, it is typical to follow the Wikipedia model. Wikipedia is published under CC-BY-SA, and publishing is centralized. However, the publisher of their own MediaWiki instance can choose any copyright model they wish.

In the Massive Wiki world, it is typical to publish under CC-BY. The centralized (static-web?) publishing presents a website that does not foreground co-editing. However, it is easy to provide download of a zip file of the whole wiki. The publisher of the wiki may choose any copyright model they wish. The reader who has downloaded a zipfile of the whole wiki has the moral right and responsibility to follow the publisher's copyright restrictions or not. (TODO: this does not make sense. If a copyright license is provided with the wiki content, then the ethical responsibility is to use that license, or contact the wiki license holder to ask for different terms. Yes?)

