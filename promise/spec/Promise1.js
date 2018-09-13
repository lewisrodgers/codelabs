const MyPromise = require('../promise1');

const JasmineConsoleReporter = require('jasmine-console-reporter');
jasmine.getEnv().addReporter(new JasmineConsoleReporter({
  verbosity: true
}));

xdescribe("Promise", function() {
  let promise;
  
  beforeEach(() => {
    promise = new MyPromise((resolve, reject) => {
      resolve("hello");
    });
  })

  it("should have a resolve function", function() {
    console.log(promise)
  })
  
  // it("should be an object", function() {
  //   expect(typeof promise).toBe('object');
  // })

  // it("should remember the list of promises", function() {
  //   expect(promise.promiseChain).toBeDefined();
  // })

  it("should resolve the promise", function() {
    const resp = promise.then((x) => { 
      console.log(x);
    });
    // expect(resp).toBe("hello");
  })

  // describe("then", function() {
  //   it("should have a `then` method", function() {
  //     expect(promise.then).toBeDefined();
  //   })

  //   it("should remember the promise", function() {
  //     promise.then(() => {})
  //     expect(promise.promiseChain.length).toBe(1)
  //   })
  // })

  // it("should have `onResolve` method", function() {
  //   expect(promise.onResolve).toBeDefined();
  // })


})