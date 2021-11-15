# Run Flask application through code

Export the required environment variables before running the application.

```sh
# export FLASK_APP=app
export FLASK_ENV=development
```

Instead of using the command line, the development server can also be started from Python with the `Flask.run()` method. This method takes arguments similar to the CLI options to control the server.

The main difference from the CLI command is that the server will crash if there are errors when reloading.

`debug=True` can be passed to enable the debugger and reloader, but the `FLASK_ENV=development` environment variable is still required to fully enable development mode.

```python
# app.py
if __name__ == "__main__":
    app.run(debug=True)
```

Add `app.run(*args, **kwargs)` in the main block, otherwise it will try to run the application when trying to import.

```sh
python app.py
```

Run the application using python.

```sh
 * Serving Flask app 'app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 197-907-973
```
