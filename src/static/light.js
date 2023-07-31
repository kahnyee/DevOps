var chartLight;

function requestData() {
  // Ajax call to get the Data from Flask
  var requests = $.get("/data");
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
    // Light
    var seriesLight = chartLight.series[0],
      shiftLight = seriesLight.data.length > 20;

    // Add the Point
    // Time Light
    var data5 = [];
    data5.push(result[0]);
    data5.push(result[5]);

    chartLight.series[0].addPoint(data5, true, shiftLight);
  });
  // call it again after one second
  setTimeout(requestData, 500);
}

$(document).ready(function () {
  // --------------Chart 5 -----------------------
  chartLight = new Highcharts.Chart({
    chart: {
      renderTo: "data-Light",
      defaultSeriesType: "area",
    },
    title: {
      text: 'Ambient Lighting Intensity ("LDR" Readings)',
    },
    xAxis: {
      type: "datetime",
      tickPixelInterval: 150,
      maxZoom: 20 * 1000,
    },
    yAxis: {
      minPadding: 0.2,
      maxPadding: 0.2,
      title: {
        text: "Value",
        margin: 80,
      },
    },
    series: [
      {
        lineColor: "#1d82b8",
        name: "Light Level",
        data: [],
      },
    ],
  });
  setTimeout(requestData, 500);
});
