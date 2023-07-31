var chartTemperature;
var chartHumidity;
var chartEC;
var chartPH;
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
    // Temperature
    var seriesTemperature = chartTemperature.series[0],
      shiftTemperature = seriesTemperature.data.length > 20;

    // Humidity
    var seriesHumidity = chartHumidity.series[0],
      shiftHumidity = seriesHumidity.data.length > 20;

    // EC
    var seriesEC = chartEC.series[0],
      shiftEC = seriesEC.data.length > 20;

    // PH
    var seriesPH = chartPH.series[0],
      shiftPH = seriesPH.data.length > 20;

    // Light
    var seriesLight = chartLight.series[0],
      shiftLight = seriesLight.data.length > 20;

    // Add the Point
    // Time Temperature
    var data1 = [];
    data1.push(result[0]);
    data1.push(result[1]);

    // Add the Point
    // Time Humidity
    var data2 = [];
    data2.push(result[0]);
    data2.push(result[2]);

    // Add the Point
    // Time EC
    var data3 = [];
    data3.push(result[0]);
    data3.push(result[3]);

    // Add the Point
    // Time PH
    var data4 = [];
    data4.push(result[0]);
    data4.push(result[4]);

    // Add the Point
    // Time Light
    var data5 = [];
    data5.push(result[0]);
    data5.push(result[5]);

    chartPH.series[0].addPoint(data4, true, shiftPH);
    chartTemperature.series[0].addPoint(data1, true, shiftTemperature);
    chartHumidity.series[0].addPoint(data2, true, shiftHumidity);
    chartLight.series[0].addPoint(data5, true, shiftLight);
    chartEC.series[0].addPoint(data3, true, shiftEC);
  });
  // call it again after one second
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
      text: 'pH Level of the Solution ("Potentiometer" Readings)',
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

  // --------------Chart 1 ----------------------------
  chartTemperature = new Highcharts.Chart({
    chart: {
      renderTo: "data-temperature",
      defaultSeriesType: "area",
    },
    title: {
      text: 'Ambient Temperature (Temperature" Readings)',
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
        name: "Temperature",
        data: [],
      },
    ],
  });

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
