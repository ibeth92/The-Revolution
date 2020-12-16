function buildPlot() {
  /* data route */
  const url = "/api/pals";
  d3.json(url).then(function (response) {

    console.log(response);

    const data = response;

    const layout = {
      scope: "usa",
      title: "Pet Pals",
      showlegend: false,
      height: 600,
      // width: 980,
      geo: {
        scope: "usa",
        projection: {
          type: "albers usa"
        },
        showland: true,
        landcolor: "rgb(217, 217, 217)",
        subunitwidth: 1,
        countrywidth: 1,
        subunitcolor: "rgb(255,255,255)",
        countrycolor: "rgb(255,255,255)"
      }
    };

    Plotly.newPlot("plot", data, layout);
  });
}

buildPlot();

// Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById('myImg');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function () {
  modal.style.display = "block";
  modalImg.src = this.src;
  modalImg.alt = this.alt;
  captionText.innerHTML = this.alt;
}

// When the user clicks on <span> (x), close the modal
modal.onclick = function () {
  img01.className += " out";
  setTimeout(function () {
    modal.style.display = "none";
    img01.className = "modal-content";
  }, 400);

}    