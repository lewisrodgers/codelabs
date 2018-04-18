# pip install --upgrade google-api-python-client google-auth google-auth-httplib2
import argparse

from google.oauth2 import service_account
import googleapiclient.discovery


parser = argparse.ArgumentParser()
parser.add_argument('useremail', help='The email of the admin user to impersonate')
parser.add_argument('domain', help='The domain to access data from')
args = parser.parse_args()


SCOPES = ['https://www.googleapis.com/auth/admin.directory.user.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

DELEGATE=args.useremail  # Service account will impersonate this user. Must have proper admin privileges in G Suite.
TARGET=args.domain  # This is the domain that the service account wants to access data from.

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials_delegated = credentials.with_subject(DELEGATE)

service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials_delegated)
response = service.users().list(domain=TARGET).execute()

print(response)