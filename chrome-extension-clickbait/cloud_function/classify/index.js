const automl = require('@google-cloud/automl');


exports.classify = (req, res) => {
  res.set('Access-Control-Allow-Origin', '*');

  if (req.method === 'OPTIONS') {
    res.set('Access-Control-Allow-Methods', 'POST');
    res.set('Access-Control-Allow-Headers', 'Content-Type');
    // res.set('Access-Control-Max-Age', '3600');
    res.status(204).send('');
  } else {
    res.set('Access-Control-Allow-Origin', '*');
    sendRes();
  }

  function sendRes() {
    // Creates a client
    const client = new automl.PredictionServiceClient();

    console.error("req...");
    console.error(req);
    console.error("req.body...");
    console.error(req.body);

    // const data = JSON.parse(req.body);
    const data = req.body;
    console.error("msg...");
    console.error(data.message)

    client
      .predict({
        name: client.modelPath('decoded-keel-200715', 'us-central1', 'TCN7312655095228328642'),
        payload: {
          textSnippet: {
            content: data.message
          }
        }
      })
      .then(responses => {
        var response = responses[0];
        res.send(response);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
