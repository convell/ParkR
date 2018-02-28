# ParkR

### Abstract

The shared parking application is introducing application as a service and sharing economy to parking. The shared parking application will be a web and mobile application that allows users to look at  a map of the area they are in, see if there are any open parking spots, and reserve that spot. Ideally, a custom map of each new area added to the application will be created to give users a simple but detailed view of their options. Owners of the spots can set when and how long the spots are available, as well as the cost of the spot. The application overall aims to reduce the amount of “wasted” private parking and open up those resources to the general public. This in turn would create a new marketplace and level of efficiency parking has never seen before.

## Working on ParkR

### SSHFS Setup (use if git is a pain, but should be a last resort)
#### OS X
1. Install Fuse and SSH https://osxfuse.github.io/
2. Run:

```sudo sshfs -o allow_other,defer_permissions -o sftp_server="/usr/bin/sudo /usr/lib/openssh/sftp-server" user@parkfor.me:/ /WhereYouWant/ToMount```
3. parkfor.me server should be mounted at /WhereYouWant/ToMount/ and ready for use
#### Linux / Debian Based
1. Install ```sudo apt-get install sshfs```
2. Run:

```sudo sshfs -o allow_other,defer_permissions -o sftp_server="/usr/bin/sudo /usr/lib/openssh/sftp-server" user@parkfor.me:/ /WhereYouWant/ToMount```
3. parkfor.me server should be mounted at /WhereYouWant/ToMount/ and ready for use
#### Windows
You are on your own ya dork

### Local Workflow
The best option is to start with a clean version of the repo, in order to do that we will run the following:

`sudo git clone https://github.com/convell/ParkR /dir/to/copy/into`

You can also obtain a working copy from SSHFS as stated above. The Django code is located in the /home/Django/directory

If you have not installed django before on this enviornment you will more than likely need to run:

`sudo pip install django netifaces`

From here you now have a working copy of django and code. We will contine in the next section on getting familar with git to save yourself the headache of rebasing the code.


### Git Workflow
#### Where to start
This section assumes you have completed the Local Workflow section. We will start work in the git clone directory. To confirm that you have cloned succesfully run `git status` and you should hopefully see a message of 
> Your branch is up-to-date with 'origin/master'

**BEFORE TOUCHING CODE:**

We will need to create a new branch for development. We will try to stay off developing the main branch, and instead create feature branches in which we merge the code into [sandbox](https://github.com/convell/ParkR/tree/sandbox). So with your cloned directory, we will run `git checkout -b <nameOfBranch>` to create a LOCAL copy of the branch with the code from master (the branch you were on before the checkout command). Now to create the branch on the remote repo you simply run `git push origin <nameOfBranch>`


**Setting up Pull Requests**
![How To Pull](https://i.imgur.com/GzgzSH4.png)
![How To Pull](https://i.imgur.com/Dfo7k3A.png)

Sandbox will be a useful staging area before master. This also allows us to solve any merge conflicts before pushing to master. This is a huge deal as we do not want to have a lapse of coverage when pulling from master to the server due to merge conflicts. To maintain the most amount of uptime it is recomended to solve any conflicts and testing before using the server. 


Because we dont know what state Sandbox was left in (hopefully everyone is pulling master into it after their pushes) it is recomended to hit the compare button (as shown above in the pull request pictures) with master going INTO sandbox. If there are changes to be made automatically go ahead and merge them. However if there are changes that cant be made automatically, find the latest commit on master and contact the author to fix sandbox with their merge conflict.


When you are done pulling master into sandbox, go ahead and pull your branch into sandbox. Fix any merge conflicts as carefully as you can. If you broke something the Circle continous integration will mark the commit with a red x, however it does not catch logic errors. So when you are done pulling to sandbox your changes, pull sandbox into your local enviornment `git checkout -b sandbox & git pull origin sandbox` for testing of features. Make sure your changes still work along with all previous features.


When all done set a pull request going from sandbox to master. Go to discord and tag parkr asking for a quick review. When that review is done the person reviewing who confirmed everything is good will close the request and merge sandbox into master.


### Server Workflow
When all done with testing in sandbox and code is merged into master, it is time for it to be in production. We can now run `git pull origin master` on parkfor.me. After the code is succesfully pulled down from github, the last step is to restart gunicorn with `systemctl restart gunicorn.service`

From there sitback and enjoy your live code changes!

## Continous Integration
[**Check our current builds!**](https://circleci.com/team/gh/convell)


Continous Integration is a current standard in most agile based workflows. However because we have very little agile practices, we are using very little continous integration. Current we are just doing a simple test to check if it crashes django on python 2.7, and with a few different test cases. If this project gets bigger we should consider writing out the config file to test more edge cases.
