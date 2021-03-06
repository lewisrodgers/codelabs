# How to use domain-wide delegation to manipulate a user's Google Calendar

The basic script in `main.py` demonstrates how one might use domain-wide delegation to access a specific user's calendar to clear their events, without requiring manual authorization from the user.

To see how domain-wide delegation fits together from a 30,000-foot-view see: [Domain-wide delegation — a visual guide](https://github.com/lewisrodgers/notes/blob/master/domain-wide-delegation-visual-guide.md)

Notice that the user's account of the calendar to be manipulated is passed to the `with_subject` method.

```
credentials_delegate = credentials.with_subject(ACCOUNT)
```

In other words: given the client wants to clear John Doe's calendar of events (or whatever the case may be), then it will impersonate John Doe by using John's email account. 

## Quick start

```
pip install pipenv
pipenv install
pipenv shell
```

In `main.py` change the `TARGET` variable with an actual user email address from your domain. Then run the script.

```
python main.py
```
