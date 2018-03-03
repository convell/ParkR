# ParkR
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
    (env) $ pip install django django-crispy-forms
```


To run the project locally:

In the main project folder (same folder with manage.py) run:
```
    $ python manage.py runserver
```

Now if you open `localhost:8000` in the browser you should see the website

**You can (and should) make and test all changes locally.**


When you are happy with all of your changes, push to the project github.
```
    $ git add .
    $ git commit -m "message"
    $ git push
```



Production
------
To make the changes live, you will need to pull them down to the server and restart gunicorn.
To get into the server, you will need to download the seniorproject_parkr.pem (sent via email). Save this somewhere you can find it easily.

Go into the same folder where you have the .pem file saved and execute this command in the terminal:
```
    $ chmod 400 seniorproject_parkr.pem **(only necessary the first time you access the server)**
    $ ssh -i "seniorproject_parkr.pem" ubuntu@ec2-52-15-198-182.us-east-2.compute.amazonaws.com
```

Once inside the server, do a git pull in the ParkR directory and restart gunicorn:
```
    $ git pull
    $ sudo systemctl restart gunicorn
```


You can now see your changes live at phoebeargon.com