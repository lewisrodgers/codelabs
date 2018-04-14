# How to use domain wide delegation to manipulate a user's calendar

This basic script demonstrates how one might use domain wide delegation to access a specific user's calendar to clear their events, without required manual authorization from the user.

Notice that you pass the user's email of the calendar you want to manipulate to the `create_delegated` method.

```
credentials_delegate = credentials.with_subject(EMAIL)
```