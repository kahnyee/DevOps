function requestData() {
  // Ajax call to get the Data from Flask
  var requests = $.get("/data_current");
  $.get("/get-switch-state", function (result) {
    var sysRunText = document.getElementById("sys-run-text");
    var circle = document.querySelector(".circle");

    if (result == 1) {
      sysRunText.innerText = "System Running";
      circle.classList.add("started");
      circle.classList.remove("stopped");
    } else if (result == -1) {
      sysRunText.innerText = "System Stopped";
      circle.classList.add("stopped");
      circle.classList.remove("started");
    }
  });

  var tm = requests.done(function (result) {
    if (result.length > 0) {
      document.getElementById("pHGraph").innerText =
        "Potentiometer Readings: " + result[4];
      document.getElementById("TempGraph").innerText =
        "Temperature Readings: " + result[1];
      document.getElementById("HumidGraph").innerText =
        "Humidity Readings: " + result[2];
      document.getElementById("LightGraph").innerText =
        "LDR Readings: " + result[5];
      document.getElementById("ECGraph").innerText = "EC Level: " + result[3];
    } else {
      // Handle the case when data is not available
      document.getElementById("pHGraph").innerText = "No data available";
      document.getElementById("TempGraph").innerText = "No data available";
      document.getElementById("HumidGraph").innerText = "No data available";
      document.getElementById("LightGraph").innerText = "No data available";
      document.getElementById("ECGraph").innerText = "No data available";
    }
  });
  // call it again
  setTimeout(requestData, 500);
}

requestData();
