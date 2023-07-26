let pageWidth = window.innerWidth;
var pos = 0;
const pacArray = [
    ['PacMan1.png', 'PacMan2.png'],
    ['PacMan3.png', 'PacMan4.png']
];
var direction = 0;
var focus = 0;

function Run() {
    let img = document.getElementById("PacMan");
    let imgWidth = img.width;
    focus = (focus + 1) % 2;
    direction = checkPageBounds(direction, imgWidth);
    img.src = pacArray[direction][focus];
    if (direction) {
        pos -= 20;
        img.style.left = pos + "px";
    } else {
        pos += 20;
        img.style.left = pos + 'px';
    
    // Use setTimeout to call Run every 200 millesecs
}
}
setInterval(Run, 200);

function checkPageBounds(direction, imgWidth) {
    //
    // Complete this to reverse direction on hitting page bounds
    //
    var size = document.body.clientWidth;
    console.log(pos,pageWidth,imgWidth);
    if (pos > pageWidth-imgWidth) {
        direction = 1;
    }
    else if (pos === 0) {
        direction = 0;
    }
    //console.log(pos);
    /*switch(pos) {
        case ():
            direction = 1;
            break;
        case 0:
            direction = 0;
            break;
    }*/
    return direction;
}