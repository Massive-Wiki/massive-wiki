# How to set up and use a Massive Wiki 

2024-03-15: some notes to scope the work needed to put a Massive Wiki into practice

-----
What are the pre-requisites for using Massive Wiki?

1. Familiar with Markdown formatting of text files  
2. Some experience using `git` and [Github](https://github.com)

----
What are the basic steps to getting a Massive Wiki working?

1. Gather the Markdown files to be worked on and shared into a folder (this folder can contain subfolders)
2. Establish this folder as a `git` repository that is hosted on Github (use `massive-wiki-publishing-kit` Github repository template?)
3. Share this repository with collaborators and establish practices to support sharing the document work (writing, reviewing, editing, etc.) (You probably already know how to work together. Using `git` is best with some rules of practice.)

-----
What are the steps needed to publish the documents on the Web?

1. Install and configure Massive Wiki Publishing Kit
	- install web theme `basso`
	- set web site configuration properties in `mwb.yaml`
2. Set up an account on a web-hosting service such as [Netlify](https://netlify.app)
3. Configure Netlify to rebuild your website when the Github repository content is updated.

