# Cloud Build

Source: https://medium.com/google-cloud/checking-javascript-with-cloud-builder-dab387f6d6ff

Use Google Cloud Build to do style checking with the JavaScript linter eslint.

```bash
cloud-build-local --config=cloudbuild.yaml --dryrun=false --push .  # build locally
gcloud builds submit . --config=cloudbuild.yaml
```

## Deply Slack notifications Cloud Function

```bash
gcloud beta functions deploy subscribe --stage-bucket staging.decoded-keel-200715.appspot.com --trigger-topic cloud-builds
```