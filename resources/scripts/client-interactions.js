let opened = false;
const showButton = document.getElementById("show-button");
const showButtonGraphics = document.getElementById("show-button-graphics");
const addConversationButtonGraphics = document.getElementById("add-conv-button-graphics");
const newConversationText = document.getElementById("new-conv");
const mainGrid = document.getElementById("main-container");

function showHideDiscussions() {
    opened = !opened;
    if (opened) {
        mainGrid.style.gridTemplateColumns = "max(300px, 30vw) auto";
        showButtonGraphics.style.d = "path('M5,40 L40,20 M5,40 L75,40 M5,40 L40,60')";
        addConversationButtonGraphics.style.d = "path('M10,40 L70,40 M40,10 L40,70')";
        newConversationText.style.bottom = "0";
        newConversationText.style.transitionDelay = "0.15s";
        document.getElementById("conversation-list").style.padding = "var(--main-padding) var(--main-padding) 0 var(--main-padding)";
    }
    else {
        mainGrid.style.gridTemplateColumns = "50px auto";
        showButtonGraphics.style.d = "path('M5,10 L75,10 M5,40 L75,40 M5,70 L75,70')";
        addConversationButtonGraphics.style.d = "path('M40,40 L40,40 M40,40 L40,40')";
        newConversationText.style.bottom = "-40px";
        newConversationText.style.transitionDelay = "0s";
        document.getElementById("conversation-list").style.padding = "var(--main-padding) var(--main-padding) 0 55px";
    }
}

showButton.addEventListener("click", showHideDiscussions, false);