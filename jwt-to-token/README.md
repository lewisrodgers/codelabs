# Usage

Install dependencies.

```bash
npm install
```

Set some environment variables.

```bash
SECRET="./path/to/secret.json"
SCOPES="scope1, scope2, ..."
AS_USER="user_email"
```

Get an access token.

```bash
TOKEN=$(bash jwt-to-token.sh $SECRET $SCOPES $AS_USER)
```

Make an API request with the token.

```bash
curl -H "Authorization: Bearer $TOKEN" https://www.googleapis.com/calendar/v3/calendars/primary
```
