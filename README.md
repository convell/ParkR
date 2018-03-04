# ParkR [![CircleCI](https://circleci.com/gh/convell/ParkR.svg?style=svg&circle-token=05d8f949d3d8bb8ee8102533e541c0a821f71207)](https://circleci.com/gh/convell/ParkR)
Senior project for CS 425

Uses Django 2.0 and Python 3


Development
------

Create the directory where you would like to store the project

Clone the project into this new directory
```
    $ git clone https://github.com/phoebeargon/ParkR.git
```

Create and activate a virtual environment to work in within your new directory (must be named env):
```
    $ python3 -m venv env
    $ . env/bin/activate
```

Install requirements for the project on your virtual environment:
```
    (env) $ pip install requirments.txt
```


To run the project locally:

In the main project folder (same folder with manage.py) run:
```
    $ python manage.py runserver
```

Now if you open `localhost:8000` in the browser you should see the website

**You can (and should) make and test all changes locally. MAKE SURE TO CHANGE BRANCHES/DONT DEVELOP ON MASTER**


Github
------

When you are happy with all of your changes, push to the project github.
```
    $ git status (make sure you are on the right branch)
    $ git add . (make sure not to drag in files like pyc)
    $ git commit -m "message"
    $ git push origin yourBranchHere
```

This will make a commit to your specfic branch. If you feel ready to move your changes along to testing, we will then move them to sandbox through pull request. This can be done through the GUI on github.com by hitting either pull request or compare on your personal branch.

After the pull request is made, go ahead and automatically pull the request into sandbox. This is where you will test to make sure your code still works.

When your code is in sandbox, we will pull it down locally for testing:
```
    $ git fetch
    $ git checkout sandbox
    $ git pull origin sandbox
```

From there run the server and test to make sure your changes still work! If everything looks good, make a pull request from sandbox to master, and tag parkr on discord for review.

**If you run into any issues working with github, feel free to contact Paul or consult our [wiki page for git](https://github.com/convell/ParkR/wiki/GitHub-Repo-Usage)**

Production
------
To make the changes live, you will need to pull them down to the server and restart gunicorn.

Once inside the server, do a git pull in the ParkR directory and restart gunicorn:
```
    $ git pull
    $ sudo systemctl restart gunicorn
```


You can now see your changes live at parkfor.me
