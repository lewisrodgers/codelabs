# pip install --upgrade google-api-python-client google-auth google-auth-httplib2

from google.oauth2 import service_account
import googleapiclient.discovery


SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

DELEGATE='<admin@domain.com>'  # Service account will impersonate this user. Must have proper admin privileges in G Suite.

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials_delegated = credentials.with_subject(DELEGATE)

service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials_delegated)
response = service.files().list(corpus='domain').execute()

print(response)

