# Working with Git

## An Apology

Git is not the only way to share and version text files, but it is technically very good at what it does.  However, it comes with some "sharp edges". People in the Massive Wiki community and the Git community at large have spent a lot of time to try to make it easier, but it's still sometimes a little prickly to work with. It's continuing to get better. In the meantime, thank you for your patience and forgiveness. :-)

If you run into problems, email us at [help@massive.wiki](mailto:help@massive.wiki), and one of our volunteers will be in touch.

## Installing Git

On Windows or Mac, installing Obsidian and then the Obsidian Git plugin is a good first step.  On Windows, also install [Git for Windows](https://git-scm.com/download/win) (64-bit).  Starting to use the Obsidian Git plugin will usually start the rest of the install process on Windows and Mac.

Linux computers usually have Git pre-installed.

## Setting Up Git Forge Authentication

If you are using a Git forge such as GitHub or Codeberg as part of your Massive Wiki workflow (either by yourself or with others), you'll need to set up Git with your authentication credentials. We'll write more about authentication later.

## Using Git

In Obsidian or Pulsar Editor, there is a Git panel you can enable, which allows for push-button control of Git. In Obsidian, use the Command Palette to find "Obsidian Git: Open Source Control View" to activate the panel.

In brief, here are the workflow steps when syncing changes up and down.  There are a lot of finer details to cover, we'll continue to improve our documentation.

### In A Repo Where You're A Member

-   pull new changes from the cloud
-   edit files locally
-   add/remove files to/from "Staged"
-   when ready, commit, with a commit message
-   pull again, to make sure any upstream changes get merged
-   push your changes to the cloud

### With A Repo Where You're Not A Member

-   fork repo into your own Git forge account
-   make changes as above
-   create a "pull request" (GitHub name) / "merge request" (GitLab name) and submit it to the original repo maintainers

## More Git Background

Git is the leading "version control" or "revision control" solution for tracking and managing changes in sets of text files.  It is open source, and was created in 2005 by Linus Torvalds.

It has been built by, and primarily used by, software developers who use it to help manage the source code changes in large and small software projects.  As such, it has always been powerful, but not necessarily easy to use.

Git comprises the software and protocol used to track changes between computers. A related tool is the "Git forge", which is a centralized cloud website that coordinates the use of Git between multiple people.  The original Git forge is GitHub, which was started in 2008.  GitHub supports many open and closed source projects for free, but they also require paid subscription for advanced uses.  GitHub was acquired by Microsoft in 2018.

Other Git forges include GitLab, Bitbucket, Codeberg, and Sourcehut.  There is also software for self-hosting a forge, including Gitea, Forgejo, and Gitolite.