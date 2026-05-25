# The Massive Wiki Project

## Mission / Vision

Massive Wiki is a movement to create a wiki _ecosystem_ (rather than just an engine) that provides classic wiki utility, with a plurality of tools and processes that enable decentralization and federation of the pages.

The Massive Wiki Project provides an answer to the question: What kind of wiki to use for local, community centered information?

Massive Wiki is a good platform for such a system. It is accessible to many authors and contributors. The text format for wiki pages is easy to learn, and a low bar to participation. Massive Wikis are decentralized; each author and contributor has a copy of the whole wiki, in text format. And Massive Wikis are inexpensive to run.  

**Why you might use a Massive Wiki:**

1. You have a collection of texts, notes, documents, etc., about a topic, a task, or a project that you want to share with others, and manage the changes that are made.  
2. You want this collection to be available to others, online or off.
3. You want to publish the collection, or part of it, to the Web.  

## Features and Benefits

### Wiki Functionality

Massive Wiki inherits some key features from the Wiki Wiki Web pattern invented by Ward Cunningham in 1994, including easy **linking** and **named pages.** The Wiki pattern is one of the best ways to organize and share text-based information and knowledge. We gratefully acknowledge Ward's gift to the world.
### Accessibility and Ease of Participation

Massive Wiki can be set up to be just a folder of text files on your authors' computer, that are as easy to edit or rearrange as any other text files on their computer. You can add authors by just asking them to use text files on their computer.

The plain text format used by Massive Wiki works with any standard operating system or computer interface device, including speech-based and legacy computers.
### Decentralization

Massive Wiki is built to diffuse information across space and time, unlike a centralized server-based wiki or website. Each author has a copy of the whole wiki, in text format. For public wikis, there's also a copy on GitHub or another public Git forge.

Anyone can archive it, share it, duplicate and change it, without any infrastructure besides their computing device—for example, a laptop, smartphone, or a tablet.

You can zip up the whole wiki easily and email the zipped-up wiki to a million friends for safekeeping or further distribution. Any recipient who can receive email and unzip a file will have the whole wiki.

A Massive Wiki is much more likely to survive for decades or centuries, even if centralized networking and computing infrastructure collapses.
## Why the name "Massive" Wiki

In "Massive Wiki", the word "Massive" is inspired by an acronym, "MaSVF". The word "Wiki" represents naming and easy linking between pages, as well as the wiki practice and culture of collaborative writing.

MaSVF stands for **Ma** rkdown, **S** hared, **V** ersioned, **F** iles.
#### Markdown

We use **Markdown** because it is a lingua franca. It is simple to learn and use, and "good enough" for many formatting needs.
#### Shared

Wiki is best when it is **shared** with others. Sharing files lets them move around, from centralized servers to decentralized servers, and from peer to peer.
#### Versioned

When page contention happens, **version** history is important to be able to do whatever manual merge is necessary.  
Version history is also handy when you want to refer to previous changes made to a page.  
#### Files

Each page is one **file.**  
Standard files are an easy and reasonably precise unit of data interchange between different computer systems.  
The plural "files" is important—a wiki needs more than one page.


## Massive Wiki Patterns  

In the Massive Wiki world, a wiki is a set of text files, stored on your computer, on other people's computers, and, optionally, stored in a "git forge" (a database hub, such as GitHub), and, perhaps, published on a website. There are many editing, viewing, and collaborating patterns that are then enabled by this layout, including:

- The publisher edits; the public views as a website; no collaboration.
- The publisher edits; anyone can download a single file or all the files, anyone can edit their copy and submit it back to the publisher.
- A small team collaborates on the text files using peer-to-peer file synchronization software, such as `syncthing`, or shared drives. The wiki may or may not be published to others.
- There are multiple publishers, each with possibly different edits. Maybe there is a hub-and-spoke publication of a wiki?

In any of these models, the publisher might be a single person, or a team of people acting as a single entity. The publisher ensures the wiki is published, and manages collaboration and publishing updates.  
Pro tip: Showing gratitude to the publishers in your community helps them keep publishing.  

For more about wiki patterns, some technology details, and IP practices, cf. [[The Massive Wiki Pattern]]  

## How to set up and use a Massive Wiki  

Some pre-requisite knowledge and know-how:  
1. Familiarity with Markdown formatting of text files  
2. Some experience using `git` and [Github](https://github.com)  

The basic steps to getting a Massive Wiki working:  
1. Gather the Markdown files to be worked on and shared into a folder (this folder can contain subfolders)  
2. Establish this folder as a `git` repository that is hosted on Github  
3. Share this repository with collaborators and establish practices to support sharing the document work (writing, reviewing, editing, etc.) (You probably already know how to work together. Using `git` to support document collaboration is best with some rules of practice.)  

The steps to publish the wiki documents on the Web:  
1. Install and configure [Markpub](https://markpub.org)  
	- set web site configuration properties in `mwb.yaml`
2. Set up an account on a web-hosting service such as [Netlify](https://netlify.app) 
3. Markpub is configured to re-publish the website when the Github repository content is updated.
