# Flask Minimal Application

## Run application using Flask command

```sh
flask run
# OR
python -m flask run
```

This would launch a simple server running on http://127.0.0.1:5000/.

```sh
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

http://127.0.0.1:5000/ can be accessed only on the local machine. To make it available to other devices in the network, add the `--host` flag to the command

```sh
flask run --host=0.0.0.0
# OR
python -m flask run --host=0.0.0.0
 ```

Suppose, the Flask application that we need to run is in `hello.py`, then we need to export the `FLASK_APP` environment variable before running the application.

```sh
export FLASK_APP=hello
```

When running the Flask application we can see the app name in the console as well.

```sh
 * Serving Flask app 'hello' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

**Note:** It is not necessary to set `FLASK_APP` environment variable if the application file name is `app.py` or `wsgi.py`. Flask would automatically pick up the file, set otherwise.

## Development Server and Debugging Mode

By default the Flask environment is set as production. This can be changed by using the `FLASK_ENV` environment variable.

```sh
export FLASK_ENV=development
flask run
```

This would run the application with a development server. In development mode, the server provides an interactive debugger and will reload when code is changed. This is intended for use only during local development. It is not designed to be particularly efficient, stable, or secure.

```sh
 * Serving Flask app 'hello' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 131-172-412
```
