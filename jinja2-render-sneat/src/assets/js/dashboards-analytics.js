/**
 * Dashboard Analytics
 */

'use strict';

(function () {
  let cardColor, headingColor, axisColor, shadeColor, borderColor;

  cardColor = config.colors.white;
  headingColor = config.colors.headingColor;
  axisColor = config.colors.axisColor;
  borderColor = config.colors.borderColor;

  // History kg chart
  // --------------------------------------------------------------------
  const historyKg = document.querySelector('#historyKgChart')
  const historyOptions = {
    chart: {
      type: 'area'
    },
    series: [{
      name: 'sales',
      data: [30,40,35,50,49,60,70,91,125]
    }],
    xaxis: {
      categories: [1991,1992,1993,1994,1995,1996,1997, 1998,1999]
    }
  }

  if (typeof historyKg !== undefined && historyKg !== null) {
    const historyChart = new ApexCharts(historyKg, historyOptions);
    historyChart.render();
  }

    // kg by field
  // --------------------------------------------------------------------
  const kgField = document.querySelector('#kgFieldChart')
  const kgFieldOptions = {
    chart: {
      type: 'area'
    },
    series: [{
      name: 'sales',
      data: [30,40,35,50,49,60,70,91,125]
    }],
    xaxis: {
      categories: [1991,1992,1993,1994,1995,1996,1997, 1998,1999]
    }
  }

  if (typeof kgField !== undefined && kgField !== null) {
    const kgFieldChart = new ApexCharts(kgField, kgFieldOptions);
    kgFieldChart.render();
  }

    // History kg chart
  // --------------------------------------------------------------------
  const kgFarm = document.querySelector('#kgFarmChart')
  const kgFarmOptions = {
    chart: {
      type: 'area'
    },
    series: [{
      name: 'sales',
      data: [30,40,35,50,49,60,70,91,125]
    }],
    xaxis: {
      categories: [1991,1992,1993,1994,1995,1996,1997, 1998,1999]
    }
  }

  if (typeof kgFarm !== undefined && kgFarm !== null) {
    const kgFarmChart = new ApexCharts(kgFarm, kgFarmOptions);
    kgFarmChart.render();
  }

})();
