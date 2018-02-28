# ParkR

### Abstract

The shared parking application is introducing application as a service and sharing economy to parking. The shared parking application will be a web and mobile application that allows users to look at  a map of the area they are in, see if there are any open parking spots, and reserve that spot. Ideally, a custom map of each new area added to the application will be created to give users a simple but detailed view of their options. Owners of the spots can set when and how long the spots are available, as well as the cost of the spot. The application overall aims to reduce the amount of “wasted” private parking and open up those resources to the general public. This in turn would create a new marketplace and level of efficiency parking has never seen before.

## Working on ParkR

### SSHFS Setup
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

We will need to create a new branch for development. We will try to stay off developing the main branch, and instead create feature branches in which we merge the code into [sandbox](https://github.com/convell/ParkR/tree/sandbox). So with your cloned directory, we will run `git checkout -b <nameOfBranch>` to create a LOCAL copy of the branch with the code from master (the branch you were on before the checkout command). Now to create the branch on the github repo you simply run `git push origin <nameOfBranch>`


### Server Workflow

## Continous Integration
https://circleci.com/team/gh/convell
