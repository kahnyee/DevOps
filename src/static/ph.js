var chartPH;

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
    var seriesPH = chartPH.series[0],
      shiftPH = seriesPH.data.length > 20;

    var data4 = [];
    data4.push(result[0]);
    data4.push(result[4]);

    chartPH.series[0].addPoint(data4, true, shiftPH);
  });
  setTimeout(requestData, 500);
}

$(document).ready(function () {
  // --------------Chart 4 -----------------------
  chartPH = new Highcharts.Chart({
    chart: {
      renderTo: "data-PH",
      defaultSeriesType: "area",
    },
    title: {
      text: 'pH level of the solution ("Potentiometer" Readings)',
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
        name: "PH Level",
        data: [],
      },
    ],
  });

  setTimeout(requestData, 500);
});
