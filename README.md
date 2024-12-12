# JK Holdings Backend

## Getting Started

### Installing Dependencies

1. **Python 3.7**

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

2. **Virtual Environment**

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. The instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

Instruction to create a virtual environment under the root project directory
(\jk-holdings-backend):
macOS/Linux:
```bash
python3 -m venv venv
```

Windows:
```bash
py -3 -m venv venv
```

Activate the virtual environment:
macOS/Linux:
```bash
. venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

If you want to switch projects or otherwise leave your virtual environment, simply run:
```bash
deactivate
```
3. **PIP Dependencies**

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Key Pip Dependacies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight SQL database.

## Set up the Database

Within the models.py file in `.api.models.models.py`, change the database_name, user and password variables to match those existing in your variable environments. If you do not have these variables, create a .env file under the project directory and populate it as follows:

```bash
database_name=#your database name
user=#your postgresql username
password=#your postgresql password
```

Instructions for setting up environment variables for your windows platform can be found [here](https://www.computerhope.com/issues/ch000549.htm).

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```
The --reload flag will detect file changes and restart the server automatically.