function MyPromise() {
  this.callbacks = [];
};
MyPromise.prototype = {
  callbacks: null,
  then: (callback) => {
    this.callbacks.push(callback);
  }
}


function Defer() {
  this.promise = new MyPromise();
}
Defer.prototype = {
  promise: null,
  resolve: function(data) {
    this.promise.callbacks.forEach((callback) => {
      callback(data)
    })
  }
}


module.exports = {
  MyPromise: MyPromise,
  Defer: Defer
};