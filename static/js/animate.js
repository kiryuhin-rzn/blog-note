var cx = document.querySelector("canvas").getContext("2d");
  var img = document.createElement("img");
  img.src = "https://eloquentjavascript.net/img/player_big.png";
  var spriteW = 48, spriteH = 60;
  img.addEventListener("load", function() {
    var cycle = 0;
    setInterval(function() {
      cx.clearRect(0, 0, spriteW, spriteH);
      cx.drawImage(img,
                   // source rectangle
                   cycle * spriteW, 0, spriteW, spriteH,
                   // destination rectangle
                   0,               0, spriteW, spriteH);
      cycle = (cycle + 1) % 8;
    }, 120);
  });