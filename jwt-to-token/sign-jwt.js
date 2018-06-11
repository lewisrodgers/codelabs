/**
 * Usage:
 * node sign-jwt.js "key" "scopes" "as"
 */

var jwt = require('jsonwebtoken');
var fs = require('fs');

var SECRET = JSON.parse(fs.readFileSync(process.argv[2]));
var SCOPES = process.argv[3];
var AS_USER = process.argv[4];

var token = jwt.sign({ 
  "iss": SECRET.client_email,
  "scope": SCOPES,
  "sub": AS_USER,
  "aud":"https://www.googleapis.com/oauth2/v4/token",
  "exp": Math.floor(Date.now() / 1000) + (60 * 60)
}, SECRET.private_key, {
  "algorithm": "RS256",
});

console.log(token);
