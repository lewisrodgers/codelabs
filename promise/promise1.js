function MyPromise(executionFunction) {
  this.promiseChain = [];

  this.onResolve = this.onResolve;

};

MyPromise.prototype.then = function(onResolve) {
  this.promiseChain.push(onResolve);
};

// MyPromise.prototype.onResolve = function() {

// };

module.exports = MyPromise;