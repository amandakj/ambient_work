 document.addEventListener("DOMContentLoaded", function(){
    setInterval(function() {
      var currentTime = new Date();
    
      var hours = currentTime.getHours();
      var minutes = currentTime.getMinutes();
      var seconds = currentTime.getSeconds();

      if (seconds < 10) {
        seconds = "0" + seconds;
      }
      if (minutes < 10) {
        minutes = "0" + minutes;
      } 
      var clockTime = hours + ":" + minutes + ":" + seconds;
    
      var clock = document.getElementById('myclock');
      clock.innerText = clockTime;
    },500);
    
    setInterval(function() {
      var compareDate = current_user_logintime;
      var currentTime = new Date()
      var diff = Math.abs(currentTime - new Date(compareDate.replace(/-/g,'/')));
      var diffDate = new Date(diff);
      var h = diffDate.getUTCHours();
      var m = diffDate.getUTCMinutes();
      var s = diffDate.getUTCSeconds();
      if ((h + m/60 + s/3600)>=current_user_hours) {
        var ex = document.getElementById('myexceeded');
        ex.innerText = "You have exceeded your preferred session duration";
      }
      if (s < 10) {
          s = "0" + s;
        }
      if (m < 10) {
          m = "0" + m;
        } 
      if (h < 10) {
          h = "0" + h;
        }
      var diffTime = h +":"+ m +":"+ s;
      var timer = document.getElementById('mytimer');
      timer.innerText = diffTime;
    },500);
    });
