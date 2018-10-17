function reqListener() {
  console.log(this.responseText);
}

var oReq = new XMLHttpRequest();
oReq.addEventListener('load', reqListener);
oReq.open('POST', 'https://us-central1-decoded-keel-200715.cloudfunctions.net/classify');
oReq.setRequestHeader('Content-Type', 'application/json');
oReq.send(JSON.stringify({"message":"hello from index.js"}));
