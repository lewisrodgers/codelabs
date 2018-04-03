function sort(list) {
  
  var res = [];
  var max = list.length;

  while (list.length !== 0) {
    var x = list.shift();

    if (res.length === 0) {
      res.push(x);
    }

    compare(x, res);

    
    // for (var i=0; i < res.length; i++) {
    //   // if (x < res[i]) {
    //   //   res.splice(i, 0, x);
    //   // } else {
    //   //   res.push(x);
    //   // }
    //   res.push(x);
    //   console.log(res)
    // }
  }

}

function compare(x, y) {
  for (var i=0; i < y.length; i++) {
    if (x < y[i]) {
      y.splice(i, 0, x);
    } else {
      continue;
    }
  }
  console.log(y);
}

sort([5,9,4,10,2,3,8,1]);


