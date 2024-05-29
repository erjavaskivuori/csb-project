# Cyber Security Base - Project I

This is a project for the Cyber Security Base course. The application contains security flaws as implementing them was part of the given instructions and therefore the application should not be used.

### Before installing the application

You should have [Python](https://wiki.python.org/moin/BeginnersGuide/Download) and [pip](https://pip.pypa.io/en/stable/installation/) installed.

### Linux/mac installation

1. Clone the repository

2. Create `.env` file and database

In the file the contents should be
```
SECRET_KEY=<your_secret_key>        # is used by the flask app
```

Create file db.sqlite3 for the database
```
$ touch db.sqlite
```

3. Create a virtual environment in the directory
```
python3 -m venv <name of your venv>
```

4. Activate the virtual environment
```
source <name of your venv>/bin/activate
```

5. Install the requirements
```
pip install -r requirements.txt
```

6. Initialize the database
```
python3 db_connection.py
```

7. Launch the application
```
flask run
```

### Windows installation (using PowerShell)

1. Clone the repository

2. Create `.env` file and database

In the file the contents should be
```
SECRET_KEY=<your_secret_key>        # is used by the flask app
```

Create file db.sqlite3 for the database
```
touch db.sqlite
```

In the file the contents should be
```
DATABASE=<name_of_your_db_file>     # is used in the initialization of database
SECRET_KEY=<your_secret_key>        # is used by the flask app
```

3. Create a virtual environment in the directory
```
Python35\python -m venv <name of your venv>
```

If you have configured the `PATH` and `PATHEXT`variables for your Python installation, you can use
```
python -m venv <name of your venv>
```

4. Activate the virtual environment
```
<name of your venv>/bin/Activate.ps1
```

5. Install the requirements
```
pip install -r requirements.txt
```

6. Initialize the database
```
python3 db_connection.py
```

7. Launch the application
```
flask run
```
