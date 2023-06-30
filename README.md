# takeNotes

A Personal Note taking application made using Django.

## Features

* Authentication and Authorisation implemented. (using django-allauth)
* Bootstrap 5 UI.
* Users can't access notes which are not owned by them.

## Installation and running application

Assuming you use virtualenv, follow these steps to download and run the takeNotes application.

```
   $ git clone https://github.com/diptanilsaha/takeNotes.git
   $ cd takeNotes
   $ virtualenv venv
   $ . venv/bin/activate
   $ pip install -r requirements.txt
```

Create the database tables and an admin user, follow the instructions.

```
   $ python manage.py migrate
   $ python manage.py createsuperuser
```

Run the server.

```
   $ python manage.py runserver
```

Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).
