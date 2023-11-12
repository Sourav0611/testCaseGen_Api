# texpregen-api
Test Expression Generator API (texpregen-api) is a Flask REST-ful based API for texpregen app for generating random test expressions (cases) for data structures and algorithms problems.

## How to run
Install ```python3 pip3 ```

Clone the repo.

```git clone https://github.com/agxpro-z/texpregen-api```

Change dir

```cd texpregen-api```

Install all dependencies and modules

```pip3 install -r requirements.txt```

Run app

```flask --app main run```

or

```flaks --app main run --debug``` to run in debug mode.

Open http://localhost:5000 in browser to check if API server is running properly.

Following output will be displayed in browser if API server is working properly.
```
{
  "name": "texpregen API Server"
}
```

# Next?
## texpregen app
texpregen-api is used by texpre-gen app and should be kept running for proper functioning of the app.

https://github.com/agxpro-z/texpregen
