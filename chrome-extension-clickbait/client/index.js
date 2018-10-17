function reqListener() {
  console.log(this.responseText);
}

const url = `https://${config.REGION}-${config.PROJECT_ID}.cloudfunctions.net/${config.FUNCTION}`;

var oReq = new XMLHttpRequest();
oReq.addEventListener('load', reqListener);
oReq.open('POST', url);
oReq.setRequestHeader('Content-Type', 'application/json');
oReq.send(JSON.stringify({"message":"hello from index.js"}));
