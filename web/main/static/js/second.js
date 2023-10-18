function piechart(all, main, name) {
  new Chart(document.getElementById("pie-chart"), {
    plugins: [ChartDataLabels],
    type: "pie",
    data: {
      labels: [name, "나머지"],
      datasets: [
        {
          backgroundColor: ["#c4302b", "#5a77bb"],
          data: [main, all - main],
        },
      ],
    },
    options: {
      plugins: {
        datalabels: {
          align: "end",
          anchor: "center",
          color: "#ffffff",
          font: {
            size: 14,
          },
          formatter: function (value, context) {
            let sum = 0;
            let dataArr = context.chart.data.datasets[0].data;
            dataArr.map((data) => {
              sum += Number(data);
            });
            let percentage = ((value * 100) / sum).toFixed(2) + "%";
            return percentage;
          },
        },
      },
      responsive: false,
      title: {
        display: true,
        text: "",
      },
    },
  });
}

function barchart(y_2019, y_2020, y_2021, name) {
  new Chart(document.getElementById("bar-chart"), {
    plugins: [ChartDataLabels],
    type: "bar",
    data: {
      labels: [2019, 2020, 2021],
      datasets: [
        {
          data: [y_2019, y_2020, y_2021],
          label: name,
          backgroundColor: "#5293e1",
          borderColor: "#5293e1",
          fill: false,
          barThickness: 50,
          // maxBarThickness: 10,
        },
      ],
    },
    options: {
      plugins: {
        datalabels: {
          align: "end",
          anchor: "end",
          formatter: function (value, context) {
            var idx = context.dataIndex;
            return context.chart.data[idx];
          },
        },
      },
      responsive: false,
      scales: {
        xAxes: [
          {
            barPercentage: 1,
          },
        ],
        yAxes: [
          {
            ticks: {
              min: 0,
              fontSize: 14,
            },
          },
        ],
      },
      title: {
        display: true,
        text: "년도별 논문 수",
      },
    },
  });
}
