# How to use domain wide delegation to manipulate a user's calendar

The basic script in `main.py` demonstrates how one might use domain wide delegation to access a specific user's calendar to clear their events, without requiring manual authorization from the user.

Notice that the user's account of the calendar to be manipulated is passed to the `with_subject` method.

```
credentials_delegate = credentials.with_subject(ACCOUNT)
```

In other words: given the client wants to clear John Doe's calendar of events (or whatever the case may be), then it will impersonate John Doe by passing in John's email account. 
