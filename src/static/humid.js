var chartHumidity;

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
    // Humidity
    var seriesHumidity = chartHumidity.series[0],
      shiftHumidity = seriesHumidity.data.length > 20;

    // Add the Point
    // Time Humidity
    var data2 = [];
    data2.push(result[0]);
    data2.push(result[2]);

    chartHumidity.series[0].addPoint(data2, true, shiftHumidity);
  });
  // call it again after one second
  setTimeout(requestData, 500);
}

$(document).ready(function () {
  // --------------Chart 2 -----------------------
  chartHumidity = new Highcharts.Chart({
    chart: {
      renderTo: "data-humidity",
      defaultSeriesType: "area",
    },
    title: {
      text: 'Relative Humidity ("Humidity" Readings)',
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
        name: "Humidity",
        data: [],
      },
    ],
  });
  setTimeout(requestData, 500);
});
