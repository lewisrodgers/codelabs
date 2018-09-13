const Rx = require('rxjs/Rx');

// Rx.Observable.of(1,2,3).map(function(x) {
//   console.log(x)
// });

const obs = new Rx.Observable(function(observer) {
  observer.next(1);
});

obs.subscribe({
  next: function(x) {
    console.log(x);
  }
})
