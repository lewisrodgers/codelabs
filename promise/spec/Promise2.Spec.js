const MyPromise = require('../promise2').MyPromise;
const Defer = require('../promise2').Defer;


describe('Promise 2', function() {
  let promise;
  
  beforeEach(function() {
    promise = new MyPromise();
  })

  it('has a callbacks property', function() {
    expect(promise.callbacks).toBeDefined();
  })
  
})

describe('Defer', function() {
  let defer;
  
  beforeEach(function() {
    defer = new Defer();
  })

  it('has a promise property', function() {
    expect(defer.promise).not.toBeNull();
  })

  it('has a callbacks property', function() {
    expect(defer.promise.callbacks).toBeDefined();
  })
  
})