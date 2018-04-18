# pip install --upgrade google-api-python-client google-auth google-auth-httplib2

from google.oauth2 import service_account
import googleapiclient.discovery


SCOPES = ['https://www.googleapis.com/auth/admin.directory.user.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

DELEGATE='lewis.rodgers@sherpademo.com'  # Service account will impersonate this user. Must have proper admin privileges in G Suite.
ACCOUNT_ACCESS='chase.crowson@sherpademo.com'  # This is the user account that the service account wants to access data from.

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials_delegated = credentials.with_subject(DELEGATE)

service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials_delegated)
response = service.calendarList().list(domain=ACCOUNT_ACCESS).execute()

print(response)

