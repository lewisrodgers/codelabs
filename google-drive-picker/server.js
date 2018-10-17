var express = require('express');
var app = express();

app.get('/', (req, res) => {
  res.sendfile('index.html');
});

app.listen(8080, () => console.log('Server started'));