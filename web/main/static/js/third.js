function good_item() {
  let good_item = document.getElementsByClassName("type_good");
  let bad_item = document.getElementsByClassName("type_bad");
  for (let i = 0; i < good_item.length; i++) {
    good_item[i].style.display = "";
  }
  for (let i = 0; i < bad_item.length; i++) {
    bad_item[i].style.display = "none";
  }
  document.getElementById("badit").className = "btn btn-outline-primary";
  document.getElementById("goodit").className = "btn btn-primary";
}
function bad_item() {
  let good_item = document.getElementsByClassName("type_good");
  let bad_item = document.getElementsByClassName("type_bad");
  for (let i = 0; i < good_item.length; i++) {
    good_item[i].style.display = "none";
  }
  for (let i = 0; i < bad_item.length; i++) {
    bad_item[i].style.display = "";
  }
  document.getElementById("goodit").className = "btn btn-outline-primary";
  document.getElementById("badit").className = "btn btn-primary";
}

function link(url) {
  window.open(url);
}

function piechart(num1, num2) {
  console.log("sdfgsdfsd")
  new Chart(document.getElementById("pie-chart"), {
    plugins: [ChartDataLabels],
    type: "pie",
    data: {
      labels: ["촉진요인", "저해요인"],
      datasets: [
        {
          backgroundColor: ["#3e95cd", "#c45850"],
          data: [num1, num2],
        },
      ],
    },
    options: {
      plugins: {
        datalabels: {
          color: "#ffffff",
          font: {
            size: 14,
          },
          formatter: function (value, context) {
            count = value + "개";
            return count;
          },
        },
      },
      responsive: false,
      title: {
        display: true,
        text: "촉진저해 비율",
      },
    },
  });
}

function linechart(data1) {
  let words = data1.split(",");
  use = [];
  year = [];
  for (i = 0; i < words.length; i += 3) {
    use.push(words[i + 2]);
    year.push(words[i] + "." + words[i + 1]);
  }
  new Chart(document.getElementById("line-chart"), {
    // plugins: [ChartDataLabels],
    type: "line",
    data: {
      labels: year,
      datasets: [
        {
          data: use,
          label: "이용수",
          borderColor: "#ffd400",
          fill: false,
        },
      ],
    },
    options: {
      // plugins: {
      //   datalabels: {
      //     align: "end",
      //     anchor: "end",
      //     formatter: function (value, context) {
      //       return value;
      //     },
      //   },
      // },
      elements: {
        line: {
          tension: 0.3, // disables bezier curves
        },
      },
      responsive: false,
      title: {
        display: true,
        text: "논문이용수",
      },
    },
  });
}
