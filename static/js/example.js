/*$(document).ready(function(){
$('button').click(function(){
  $('#one').animate({
    width: '500px'
  },3000, 'swing'
  ) ;
  $('#two').animate({
    width: '500px'
  },3000, 'linear'
  ) ;
});
})*/

$(document).ready(function(){
    $('#displayAnimate').click(function(){
        $("#dis").animate({
            left: 600
        }, 5000);
    });
});




document.getElementById("demo").innerHTML = "Привет Мир!";



function a(){
    var s = document.getElementById("demon");
    s.innerHTML = Date();//"Ehhhhh";
}

//a();
var id = setInterval(a, 1000);

//document.write(Date());

function changeText(id) {
  id.innerHTML = "Oooпс!";
}


function displayDate() {
  document.getElementById("demons").innerHTML = Date();
}

function displayText() {
  document.getElementById("mous").innerHTML = 'Мышь';
}

function displayText2() {
  document.getElementById("mous").innerHTML = '';
}
//var id = setInterval(displayText2, 5000);


var delay = 1000;
var currentIndex = 0;
var im = ["<img src=\'https://i.pinimg.com/564x/af/a4/4e/afa44ee17149357b2a8d69b37986242f.jpg'>",
        "<img src=\'https://flomaster.club/uploads/posts/2021-10/thumbs/1634033543_7-flomaster-club-p-sketchi-personazhei-emotsii-krasivo-7.png'>"];



function displayImage(currentIndex) {

    setTimeout(function() {
        document.getElementById("imagess").innerHTML =im[currentIndex];
    }, delay*currentIndex);

}
function der(){
  for(var currentIndex=0; currentIndex<im.length;
 currentIndex++) {
        displayImage(currentIndex);
}
}
//setTimeout(displayImage, 3000);

var animationInterval;
var spriteSheet = document.getElementById("sprite-image");
var widthOfSpriteSheet = 1472;
var widthOfEachSprite = 184;

function stopAnimation() {
  clearInterval(animationInterval);
}

function startAnimation() {
  var position = widthOfEachSprite; //start position for the image
  const speed = 100; //in millisecond(ms)
  const diff = widthOfEachSprite; //difference between two sprites

  animationInterval = setInterval(() => {
    spriteSheet.style.backgroundPosition = `-${position}px 0px`;

    if (position < widthOfSpriteSheet) {
      position = position + diff;
    } else {
      //increment the position by the width of each sprite each time
      position = widthOfEachSprite;
    }
    //reset the position to show first sprite after the last one
  }, speed);
}

//Start animation
startAnimation();















