from google.oauth2 import service_account
import googleapiclient.discovery


SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # path to json key file generated after creating a service account with DwD enabled.
TARGET='user.lumapps@sherpademo.com'  # Service account wants to access data from this account.

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials_delegated = credentials.with_subject(TARGET)


# 1. We'll use this function in #4. 
def print_status(header):
        print(header['status']) # just print the status code

# 2. Build the service.
service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials_delegated)

# 3. Build the request. Returns an HttpRequest object.
request = service.calendars().clear(calendarId='primary')

# 4. We need to explicitly ask for the response header, which is where the status
# code will be. Pass in the function from #1 that handles the response header.
request.add_response_callback(print_status)

# 5. Now, issue the request.
response = request.execute() # The target's primary calendar.
