#!/bin/bash

# Usage:
# TOKEN=$(bash jwt-to-token.sh secret.json "https://www.googleapis.com/auth/calendar" "user.lumapps@sherpademo.com")

SECRET=$1
SCOPES=$2
AS_USER=$3

JWT=$(node sign-jwt.js $SECRET $SCOPES $AS_USER)

echo $(curl https://www.googleapis.com/oauth2/v4/token -d "grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=$JWT" | jq -r ".access_token")
