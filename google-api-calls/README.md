## About

Python boilerplate for service account oauth setup to return data from a Google API.

## Dev dependencies

```
$ virtualenv env
$ . env/bin/activate
$ pip install -r requirements.txt
```

## GCP prequisites

- Enable the necessary APIs (calendar, drive, gmail, etc.) in Cloud Console 
- Create a service account, download the json key file, and enable domain wide delegation (DwD)
- Determine the required scopes (calendar readonly, drive read/write, etc.)
- In the G Suite console, an admin authorizes the service account (client ID) with the specified scopes 
- The admin also identifies an account — with proper admin privileges — that the service account will impersonate (when you want to access user's data without manual authorization from the user)

With the above in place, you or another developer, who has the json key file, can run the python code.

For documentation on how to do with Java see: https://developers.google.com/api-client-library/java/google-api-java-client/oauth2#service_accounts

## Errors

**"unauthorized_client: Client is unauthorized to retrieve access tokens using this method."**

Most likely means the service account hasn't been authorized in the G Suite console properly. Perhaps the scopes haven't been applied.

**"Not Authorized to access this resource/api"**

The delegate user account doesn't have proper privileges to access the requested resource. https://stackoverflow.com/questions/42784640/client-is-unauthorized-to-retrieve-access-tokens-using-this-method-gmail-api-c-s

**Gmail API returns 403 error code and “Delegation denied for...”**
  
https://stackoverflow.com/questions/26135310/gmail-api-returns-403-error-code-and-delegation-denied-for-user-email
