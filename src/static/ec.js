var chartEC;

function requestData() {
  // Ajax call to get the Data from Flask
  var requests = $.get("/data");
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
    var seriesEC = chartEC.series[0],
      shiftEC = seriesEC.data.length > 20;

    var data3 = [];
    data3.push(result[0]);
    data3.push(result[3]);

    chartEC.series[0].addPoint(data3, true, shiftEC);
  });
  setTimeout(requestData, 500);
}

$(document).ready(function () {
  // --------------Chart 3 -----------------------
  chartEC = new Highcharts.Chart({
    chart: {
      renderTo: "data-EC",
      defaultSeriesType: "area",
    },
    title: {
      text: 'EC Level ("Moisture Sensor" Readings)',
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
        name: "EC Level",
        data: [],
      },
    ],
  });
  setTimeout(requestData, 500);
});
