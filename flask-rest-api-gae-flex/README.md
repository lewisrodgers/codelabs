https://auth0.com/blog/developing-restful-apis-with-python-and-flask/#why-python

# About

To deploy and run this application in App Engine flexible:

`app.yaml` is required to be able to deploy to App Engine. Note the `entrypoint` keyword and the use of `gunicorn`.

`requirements.txt` is also required so that App Engine knows to install the proper dependencies when it's deployed.


# Dev dependencies

```
pipenv install
pipenv shell
```

# Serve locally

```
gunicorn -b :8080 app.main:app
```

# Usage

Get income

```
curl http://localhost:8080/incomes
```

Add new income

```
curl -X POST -H "Content-Type: application/json" -d '{
  "description": "lottery",
  "amount": 1000.0
}' http://localhost:8080/incomes
```