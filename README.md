# Cyber Security Base - Project I

This is a project for the Cyber Security Base course. The application contains security flaws as implementing them was part of the given instructions and therefore the application should not be used. If you are interested, you can [read my essay]() about fixing the security flaws!

### Before installing the application

You should have [Python](https://wiki.python.org/moin/BeginnersGuide/Download) and [pip](https://pip.pypa.io/en/stable/installation/) installed.

### Linux/mac installation

1. Clone the repository

2. Create a virtual environment in the directory
```
python3 -m venv <name of your venv>
```

3. Activate the virtual environment
```
source <name of your venv>/bin/activate
```

4. Install the requirements
```
pip install -r requirements.txt
```

5. Launch the application
```
flask run
```

### Windows installation (using PowerShell)

1. Clone the repository

2. Create a virtual environment in the directory
```
Python35\python -m venv <name of your venv>
```

If you have configured the `PATH` and `PATHEXT`variables for your Python installation, you can use
```
python -m venv <name of your venv>
```

3. Activate the virtual environment
```
<name of your venv>/bin/Activate.ps1
```

4. Install the requirements
```
pip install -r requirements.txt
```

5. Launch the application
```
flask run
```