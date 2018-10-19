const exampleModelResponse = {
  "payload":[
    {"annotationSpecId":"","displayName":"clickbait","classification":{"score":0.9152950048446655},"detail":"classification"},
    {"annotationSpecId":"","displayName":"no_clickbait","classification":{"score":0.08470500260591507},"detail":"classification"}
  ],
  "metadata":{}
};

describe("Classify", function() {
  let classify;

  beforeEach(function() {
    document.getElementById('fixture').innerHTML = `
      <h2>Hello</h2>
    `;
    const headings = document.getElementById('fixture').getElementsByTagName('h2');
    const h2 = headings[0];

    classify = new Classify();
    classify.headline(h2);
  })

  afterEach(function() {
    document.getElementById('fixture').innerHTML = '';
  })

  describe("model endopint configuration", function() {
    const config = {
      REGION: 'us-east1',
      PROJECT_ID: 'foo',
      FUNCTION_NAME: 'bar'
    };

    beforeEach(function() {
      classify.model(config);
    })

    it("should set properly formatted cloud function endpoint url", function() {
      const url = 'https://us-east1-foo.cloudfunctions.net/bar';
      expect(classify.endpoint).toBe(url)
    })
  })

  describe("predict", function() {
    describe("input", function() {
      
      beforeEach(function() {
        spyOn(classify, 'predict');
        classify.send();
      })
  
      it("should call the cloud function endpoint", function() {
        expect(classify.predict).toHaveBeenCalledWith('Hello');
      })
    })
  
    describe("output", function() {
      const data = exampleModelResponse;
  
      beforeEach(function() {
        classify.handleResponse(data);
      })
  
      it("should insert `displayName` property of response into original HTML heading element", function() {
        expect(classify.elem.innerHTML).toBe(data.payload[0].displayName);
      })
    })
  })

  
})