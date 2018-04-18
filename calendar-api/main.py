from google.oauth2 import service_account
import googleapiclient.discovery


SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # path to json key file generated after creating a service account with DwD enabled.
TARGET='replace.me@domain.com'  # Service account wants to access data from this account.

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials_delegated = credentials.with_subject(TARGET)

service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials_delegated)
response = service.calendars().clear(calendarId='primary').execute() # The target's primary calendar.

print(response)
