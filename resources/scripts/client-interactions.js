let opened = false;

function showHideDiscussions() {
    opened = !opened;
    if (opened) {
        $("#main-container").css("grid-template-columns", "max(300px, 30vw) auto");
        $("#show-button-graphics").css("d", "path('M5,40 L40,20 M5,40 L75,40 M5,40 L40,60')");
        $("#add-conv-button-graphics").css("d", "path('M10,40 L70,40 M40,10 L40,70')");
        $("#new-conv").css("bottom", "0");
        $("#new-conv").css("transition-delay", "0.15s");
        $("#conversation-list").css("padding", "var(--main-padding) var(--main-padding) 0 var(--main-padding)");
    }
    else {
        $("#main-container").css("grid-template-columns", "50px auto");
        $("#show-button-graphics").css("d", "path('M5,10 L75,10 M5,40 L75,40 M5,70 L75,70')");
        $("#add-conv-button-graphics").css("d", "path('M40,40 L40,40 M40,40 L40,40')");
        $("#new-conv").css("bottom", "-40px");
        $("#new-conv").css("transition-delay", "0s");
        $("#conversation-list").css("padding", "var(--main-padding) var(--main-padding) 0 55px");
    }
}

function moderationSwitchTab(i) {
    $("#moderation-tabs li button").css("background-color", "var(--color-cstm-blue-dark)");
    $("#moderation-tabs li button").css("color", "var(--color-text-semilight)");
    $("#moderation-tabs li button").css("transform", "scale(1)");

    $("#moderation-tabs li:nth-child("+i+") button").css("background-color", "var(--color-cstm-blue)");
    $("#moderation-tabs li:nth-child("+i+") button").css("color", "var(--color-text-light)");
    $("#moderation-tabs li:nth-child("+i+") button").css("transform", "scale(1.1)");
    
    switch (i) {
        case 1:     //Conversations
            $("#conversations-list").css("display", "flex");
            $("#users-list").css("display", "none");
            break;
        
        case 2:     //Users
            $("#conversations-list").css("display", "none");
            $("#users-list").css("display", "flex");
            break;
    
        default:
            $("#conversations-list").css("display", "none");
            $("#users-list").css("display", "none");
            break;
    }
}

$("#show-button").click(function(){showHideDiscussions()});
$("#moderation-tabs li").click(function(){moderationSwitchTab($(this).index() + 1)});
moderationSwitchTab(1);

$("#new-message").emojioneArea();