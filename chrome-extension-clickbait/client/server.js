var express = require("express");

var app = express();
app.use(express.static(__dirname));

app.get("/", (req, res) => {
  res.sendfile("index.js");
});

app.listen(8080, () => console.log("Server started"));
