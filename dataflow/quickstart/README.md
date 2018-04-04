https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python

# Dev dependencies

```
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

# Run locally

```
python local.py
```

# Run on GCP

Place `corpus.txt` in a Cloud Storage bucket.

Before running your pipeline, you must authenticate with the Google Cloud Platform. Create a service account and set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the file path of the JSON file that contains your service account key.

```
export GOOGLE_APPLICATION_CREDENTIALS="/Users/lewis/Documents/path/to/credentials.json"
```

The `remote.py` uses `argparse` so that we can pass in pipeline options through the command-line.

```
python remote.py \
  --input $BUCKET/corpus.txt \
  --output $BUCKET/results/output \
  --project $PROJECT \
  --staging_location $BUCKET/staging \
  --temp_location $BUCKET/temp \
  --runner DataflowRunner \
  --job_name my-job
```
