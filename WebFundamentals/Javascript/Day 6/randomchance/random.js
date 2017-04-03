var winNum = (Math.trunc(Math.random() * 100));
function quarterNum(x){
  for (var i = x; i > 0; i--){
    if ((Math.trunc(Math.random() *100)) == winNum){
      x = x + (Math.floor(Math.random() * 50)+50)
      console.log("winner")
    }
  }
  console.log("you lose")
}
quarterNum(10);
