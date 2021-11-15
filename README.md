# Python Flask Web Application Tutorials

Consists of a list of basic tutorials needed for flask web application develpoment.

Each tutorial has its own directory in the naming format of `tutorial([0-9]*)` and consists of its own files and folders i.e, the structure might change for each tutorial directory.  

Before running the application make sure to be in the intended tutorial directory by using the change directory command.

## Setup Virtual Environment

Install and setup virtual environment in the [main directoy].

```sh
# Install virtualenv if not available
python -m pip install --user virtualenv

# Create a virtualenv named venv
virtualenv venv
```

There is a [main requirements.txt] and each directory would have its own `requirements.txt`. Use the requirements file in the tutorial directory to install the dependencies.

For example

```sh
cd tutorial01
pip install -r requirements.txt
```

## Documentations

[Flask] version 2.0.x  
[virtualenv] installation

<!-- Links -->
[Flask]: https://flask.palletsprojects.com/en/2.0.x/
[virtualenv]: https://virtualenv.pypa.io/en/latest/installation.html

[main directoy]: ./
[main requirements.txt]: ./requirements.txt
