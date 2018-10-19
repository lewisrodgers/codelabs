

const headlines = document.getElementsByTagName('h2');

for (let i = 0; i < headlines.length; i++) {
  const classify = new Classify(headlines[i]);

  classify.model({
    REGION: config.REGION,
    PROJECT_ID: config.PROJECT_ID,
    FUNCTION_NAME: config.FUNCTION_NAME
  });
  
  classify.send();
}
