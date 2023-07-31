class CustomImage {
  constructor(size) {
    this.size = size;
  }

  backgroundImage() {
    var img = document.querySelector(".jumbotron img");
    img.style.width = "100%";
    img.style.height = "100%";
  }

  centerTitle() {
    var t1 = document.querySelector("#title");
    t1.classList.add("text-black");
    t1.classList.add("text-center");
    t1.classList.add("display-3");
  }
}

const size = "25";
var obj = new CustomImage(size);
obj.backgroundImage();
obj.centerTitle();

function requestData() {
  // Ajax call to get the Data from Flask
  var requests = $.get("/data_current");
  $.get("/get-switch-state", function(result) {
    var sysRunText = document.getElementById("sys-run-text");
    var circle = document.querySelector(".circle");

    if (result == 1) {
      sysRunText.innerText = "System Running";
      circle.classList.remove("stopped");
    } else if (result == -1) {
      sysRunText.innerText = "System Stopped";
      circle.classList.add("stopped");
    }
  });

  var tm = requests.done(function (result) {
    if (result.length > 0) {
      document.getElementById("pHGraph").innerText =
        "Current pH level of the solution ('Potentiometer' readings): " +
        result[4];
      document.getElementById("TempGraph").innerText =
        "Current Ambient Temperature ('Temperature' readings): " + result[1];
      document.getElementById("HumidGraph").innerText =
        "Current Relative Humidity ('Humidity' readings): " + result[2];
      document.getElementById("LightGraph").innerText =
        "Current Ambient lighting intensity ('LDR' readings): " + result[5];
      document.getElementById("ECGraph").innerText =
        "Current EC level ('Moisture sensor' readings): " + result[3];
    } else {
      // Handle the case when data is not available
      document.getElementById("pHGraph").innerText = "No data available";
      document.getElementById("TempGraph").innerText = "No data available";
      document.getElementById("HumidGraph").innerText = "No data available";
      document.getElementById("LightGraph").innerText = "No data available";
      document.getElementById("ECGraph").innerText = "No data available";
    }
  });

  // call it again after one second
  setTimeout(requestData, 500);
}

requestData();
