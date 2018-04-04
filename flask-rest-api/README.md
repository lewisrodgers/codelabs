https://auth0.com/blog/developing-restful-apis-with-python-and-flask/#why-python

# Dev dependencies

```
pipenv install
pipenv shell
```

# Serve

```
./serve.sh
```

# Usage

Get income

```
curl http://localhost:5000/incomes
```

Add new income

```
curl -X POST -H "Content-Type: application/json" -d '{
  "description": "lottery",
  "amount": 1000.0
}' http://localhost:5000/incomes
```