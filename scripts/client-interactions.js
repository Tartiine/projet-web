let opened = false;
const showButton = document.getElementById("show-button");
const mainGrid = document.getElementById("main-container");

function showHideDiscussions() {
    opened = !opened;
    if (opened) { mainGrid.style.gridTemplateColumns = "520px auto"; }
    else { mainGrid.style.gridTemplateColumns = "50px auto"; }
}

showButton.addEventListener("click", showHideDiscussions, false);