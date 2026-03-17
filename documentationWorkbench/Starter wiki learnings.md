# Starter wiki learnings (Bill)

2022-07-29

Reflections on using the massive-wiki-starter as the template for a personal Massive Wiki.

- Massive Wiki pre-requisites:
	- make decisions on (1) authoring, (2) sharing, (3) versioning, and (4) having a public web site of wiki content.
	- (1) authoring: Obsidian (or other app) to create Markdown files
	- (2) sharing: Github (or other Git repository hosting) is one choice
	- (3) versioning (is provided by Git repositories)
	- (4) public web site requires web hosting (netlify.app is one option)
- Decisions made; let's get started:
	- choose a folder on your computer to contain your wiki content (Bill uses ~/Documents/myWikis/ as the base and create a different folder for each wiki)
	- we are using Github, so this is one way to proceed:
	- (1) general outline: use massive-wiki-starter repository code to populate the new wiki-repository (download .zip file? fork the repo?); initialize this content into its own Github repository; configure and add the MWB and MWT submodules (this is getting complicated); make sure everything is up-to-date; push the current state as a baseline version of this new wiki(?)
	- (2022-07-31 update: https://cli.github.com/manual has some useful examples of how to proceed with a starter-wiki repository:   
		e.g., `$ gh repo create mynewrepo --public --source=. --remote=upstream`
		also see [[Github - getting started notes]]

	- (2) edit the README.md file with information you want on your wiki home-page
		- since we said "yes, we want a public website" now is the time to edit the MassiveWikiBuilder configuration file `.massivewikibuilder/mwb.yaml` , cf. [[MWB configuration]]
		- using a Sidebar? now is the time to add content to [[Sidebar]]
		- since we are implementing a Sidebar now is the time to edit `wiki_dir/netlify.toml` and insure that the mwb command is using the basso theme
