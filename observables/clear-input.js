// custom event

function fromEvent(target, eventName) {
  return new Rx.Observable((observer) => {
    const handler = (e) => observer.next(e);

    target.addEventListener(eventName, handler);

    return () => {
      target.removeEventListener(eventName, handler);
    };
  });
}

const ESC_KEY = 27;
const nameInput = document.getElementById('name');

const subscription = fromEvent(nameInput, 'keydown').subscribe((e) => {
  if (e.keyCode === ESC_KEY) {
    nameInput.value = '';
  }
});