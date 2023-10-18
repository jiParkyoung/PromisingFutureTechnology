function wordcloud(key) {
  let words = key.split(",");
  data = [];
  for (i = 0; i < words.length; i += 2) {
    data.push({ x: words[i], value: words[i + 1] });
  }

  chart = anychart.tagCloud(data);
  chart.angles([0]);
  chart.textSpacing(13);
  chart.container("container");
  chart.tooltip().format("비율 : {%yPercentOfTotal}% ({%value}개)");
  chart.draw();

  // configure tooltips

  chart.listen("pointClick", function (e) {
    location.href = e.point.get("x");
  });
  document.getElementsByClassName("anychart-credits")[0].style.display = "none";
}

function remove_pdf(s) {
  str = s.slice(-4);
  return str;
}
