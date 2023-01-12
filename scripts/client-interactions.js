let opened = false;
const showButton = document.getElementById("show-button");
const showButtonGraphics = document.getElementById("show-button-graphics");
const mainGrid = document.getElementById("main-container");

function showHideDiscussions() {
    opened = !opened;
    if (opened) {
        mainGrid.style.gridTemplateColumns = "max(300px, 30vw) auto";
        showButtonGraphics.style.d = "path('M5,40 L40,20 M5,40 L75,40 M5,40 L40,60')";
        document.getElementById("conversation-list").style.padding = "var(--main-padding) var(--main-padding) 0 var(--main-padding)";
    }
    else {
        mainGrid.style.gridTemplateColumns = "50px auto";
        showButtonGraphics.style.d = "path('M5,10 L75,10 M5,40 L75,40 M5,70 L75,70')";
        document.getElementById("conversation-list").style.padding = "var(--main-padding) var(--main-padding) 0 55px";
    }
}

showButton.addEventListener("click", showHideDiscussions, false);