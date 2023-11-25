# texpregen-api
Test Expression Generator API (texpregen-api) is a Flask REST-ful based API for texpregen app for generating random test expressions (cases) for data structures and algorithms problems.

## Getting started
### Prerequisite
- Python3
- Pip3
- Flask
- Flask-Cors
- Flask-RESTful

### How to run
- Installing ```python3``` and ``` pip3 ```

    Download and install python3 from https://www.python.org/downloads/ or follow your machine platform specific guide to install python.

- Cloning the repository
    ```
    git clone https://github.com/agxpro-z/texpregen-api
    ```

- Changing to 'texpregen-api' directory
    ```
    cd texpregen-api
    ```

- Installing all dependencies and modules
    ```
    pip3 install -r requirements.txt
    ```

- Running app
    ```
    flask --app main run
    ```

    or

    ```
    flask --app main run --debug
    ```

    to run in debug mode.

Open [http://localhost:5000](http://localhost:5000) in browser to check if API server is running properly.

Following output will be displayed in browser if API server is working properly.
```
{
  "name": "texpregen API Server"
}
```

# Next?
## texpregen app
texpregen-api is used by texpregen app and it should be kept running for proper functioning of the app.

https://github.com/agxpro-z/texpregen
