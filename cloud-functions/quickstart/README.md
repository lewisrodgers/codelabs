https://cloud.google.com/functions/docs/quickstart

```
$ gcloud functions deploy hello --trigger-http
$ curl https://[GCP_REGION]-[PROJECT_ID].cloudfunctions.net/hello
```

The fully qualified https trigger url is provided after deploying the function. If the function is already deployed you can use `gcloud` or visit the Cloud Console to get the url.

```
$ gcloud functions describe hello
```
