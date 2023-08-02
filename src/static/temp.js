var chartTemperature;

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
    var seriesTemperature = chartTemperature.series[0],
      shiftTemperature = seriesTemperature.data.length > 20;

    var data1 = [];
    data1.push(result[0]);
    data1.push(result[1]);
    chartTemperature.series[0].addPoint(data1, true, shiftTemperature);
  });
  setTimeout(requestData, 500);
}

$(document).ready(function () {
  // --------------Chart 1 ----------------------------
  chartTemperature = new Highcharts.Chart({
    chart: {
      renderTo: "data-temperature",
      defaultSeriesType: "area",
    },
    title: {
      text: 'Ambient Temperature ("Temperature" Readings)',
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
        color: "#c23d23",
        lineColor: "#303030",
        name: "Temperature",
        data: [],
      },
    ],
  });
  setTimeout(requestData, 500);
});
