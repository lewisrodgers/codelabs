function sequenceSubscriber(observer) {
  observer.next(1);
  observer.next(2);
  observer.complete();

  return {
    unsubscribe() {}
  };
}



const sequence = new Rx.Observable(sequenceSubscriber);

sequence.subscribe({
  next(num) { console.log(num); },
  complete() { console.log('Done'); }
});


// alternative
const foo = Rx.Observable.of(1,2,3);

foo.subscribe({
  next(num) { console.log(num); },
  complete() { console.log('Done'); }
});
