function sum(){
          var summa_real = parseFloat(document.getElementById("summa_real").value);
          var s1 = parseFloat(document.getElementById("first").value);
          var s2 = parseFloat(document.getElementById("second").value);
          var s3 = parseFloat(document.getElementById("three").value);
          var s4 = parseFloat(document.getElementById("four").value);
          var s5 = parseFloat(document.getElementById("five").value);
          var s6 = parseFloat(document.getElementById("six").value);
          var s7 = parseFloat(document.getElementById("seven").value);
          var s8 = parseFloat(document.getElementById("eight").value);
          var s9 = parseFloat(document.getElementById("nine").value);
          var s10 = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9;
          var x = summa_real/s10;
          var ss1 = (x*s1).toFixed(2);
          var ss2 = (x*s2).toFixed(2);
          var ss3 = (x*s3).toFixed(2);
          var ss4 = (x*s4).toFixed(2);
          var ss5 = (x*s5).toFixed(2);
          var ss6 = (x*s6).toFixed(2);
          var ss7 = (x*s7).toFixed(2);
          var ss8 = (x*s8).toFixed(2);
          var ss9 = (x*s9).toFixed(2);
          var procent = (ss1/s1)*100;
          var sum_ss = (x*s1 + x*s2 + x*s3 + x*s4 + x*s5 + x*s6 + x*s7 + x*s8 + x*s9).toFixed(2);
          var rez1 = document.getElementById("rez1").innerText = '1) ' + ss1;
          var rez2 = document.getElementById("rez2").innerText = '2) ' + ss2;
          var rez3 = document.getElementById("rez3").innerText = '3) ' + ss3;
          var rez4 = document.getElementById("rez4").innerText = '4) ' + ss4;
          var rez5 = document.getElementById("rez5").innerText = '5) ' + ss5;
          var rez6 = document.getElementById("rez6").innerText = '6) ' + ss6;
          var rez7 = document.getElementById("rez7").innerText = '7) ' + ss7;
          var rez8 = document.getElementById("rez8").innerText = '8) ' + ss8;
          var rez9 = document.getElementById("rez9").innerText = '9) ' + ss9;
          var rez_proc = document.getElementById("rez_proc").innerText = '% ' + procent;
          var sum_ss = document.getElementById("sum_ss").innerText = 'Cверься = ' + sum_ss;
        }
        document.getElementById("go").onclick = function() {
          sum();
        }