const colors = [
    "blue",
    "black",
    "magenta",
    "purple",
    "brown",
    "grey",
    "burgundy",
    "orange",
    "blue",
    "green"
];

var velocity = 1;
var positionBall_left = 0;
var positionBall_right = 600;
var leftBall = document.getElementById("ball_left");
var rightBall = document.getElementById("ball_right");
var reverse = false;

function moveBall(){
  var positionBall_min = 0;
  var positionBall_max = 275;
  if (reverse == false){
    positionBall_left = positionBall_left + velocity; 
    positionBall_right = positionBall_right - velocity;
  }
  else {
    positionBall_left = positionBall_left - velocity; 
    positionBall_right = positionBall_right + velocity;
  }
  
  if (positionBall_left==positionBall_min){reverse=false}
  if (positionBall_left>positionBall_max){reverse=true}
  if (positionBall_left==positionBall_max){
    leftBall.style.background = colors[Math.floor(Math.random() * 10)];
    rightBall.style.background = colors[Math.floor(Math.random() * 10)];
  }

  leftBall.style.left = positionBall_left + "px";
  rightBall.style.left = positionBall_right + "px";
}

setInterval(moveBall, 5);