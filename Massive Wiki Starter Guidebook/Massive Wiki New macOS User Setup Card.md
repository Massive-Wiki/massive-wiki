# Massive Wiki new macOS user setup
#### Last edit: 2021-06-15, Bill Anderson

## Pre-requisites

	- GitHub account
	- GitHub access to a Massive Wiki GitHub repository
	- Install GitHub Desktop App from https://desktop.github.com

## Set up Massive Wiki tools and credentials

1. Install Obsidian from https://obsidian.md

2. Install the Obsidian-Git plugin

   Enabling Obsidian-Git brings up a message requiring installation of command line developer tools. Select "Install ".

3. Connect Obsidian to a Massive Wiki repository

   - Open GitHub Desktop and login.
   - Use GitHub Desktop to clone the Massive Wiki repository to which you have access.
   - Open Obsidian and open another vault using the cloned repository directory as the new vault folder.

4. Set up GitHub Personal Access Token credentials to allow saving new and edited wiki files to the GitHub repository.

5. Using a GitHub Personal Access Token to resolve the

    	  fatal: could not read username for 'https://github.com'

   error when first pushing changes to GitHub.

  - How to do that
	- Use a browser and login to your GitHub account.
    - GoTo " Account Settings".
    - on "Account Settings" page select "Developer Settings" from the LeftSide buttons.
    - on "Developer Settings" page select "Personal access tokens" button.
    - on "Personal access tokens" page select "Generate new token" button.
      - on "New personal access token" page
	  - Enter a name or descriptor word into the "Note" field.
	  - Select the "repo" radio button in the "Select scopes" list.
	  - Scroll to the bottom and select "Generate token"
	  - Select the small 'copy' icon next to the new generated token to copy key to the clipboard.
	  (I also take a screen snapshot of the window with the token for a temporary backup.)

  - The final steps involve adding information to the `.gitconfig` file and creating a `.git-credentials` file to hold the personal access token just generated.
    - Setting up git credentials for Massive Wiki use.
    - First, open a Terminal window (Terminal is found in the /Applications/Utilities/ directory) and verify that a .gitconfig file has been created in the $HOME directory (when you installed GitHub Desktop and logged into GitHub)

          		$ cd
		        $ ls .gitconfig
		  
      will print the file name ".gitconfig" if it exists.

   - Second, use git commands to set up using the personal access key
      (this command says credentials are stored in a local file named ".git-credentials").

         $ git config --global credential.helper store

   - Third, create the credential file to hold the personal access key.
      Copy the personal access key generated in GitHub to the clipboard (if you did not do that above)
      Now, type the following in the terminal window replacing "YourGitHubUserName" with your actual GitHub user name:
  
         $ echo "https://YourGitHubUserName:$(pbpaste)@github.com" > .git-credentials

##### Obsidian-Git will now be able to push changes to the repository.





