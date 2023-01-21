/*username = $('#username').html()
if(username != ""){
    console.log(username)
}else{
    console.log("no username")
}

function generateChat(messages){
    str = ""
    for(message of messages){
        if(message.author.username == username){
            str += "<div class=\"message-me\">\n"
        }else{
            str += "<div class=\"message-other\">\n"
        }
        str += "<p>" + message.author.username + "</p>\n"
        str += "<p>" + message.content + "</p>\n"
        str += "<p>" + message.publication_date + "</p>\n"
        str += "</div>\n"
    }
    return str
}

function loadChat(chatname){
    console.log("loading : ")
    console.log(chatname)
    $.ajax('http://localhost:8000/chat/getMessages', {
        method:'GET',
        data: {
            "chatName":chatname,
        },
    }).done( response => {
        console.log(response)
        $("#conversation-thread").html(generateChat(response.messages))
        $("#conversation-thread").get(0).scrollTo(0, $("#conversation-thread").get(0).scrollHeight);
        console.log($("#conversation-title h3").html(chatname))
    })
}

function sendMessage(chat,content){
    $.ajax('http://localhost:8000/chat/saveMessage', {
        method:'POST',
        data: {
            "chat":chat,
            "content":content,
        },
    }).done( response => {
        console.log(response)
        if(response.messages) {
            $("#conversation-thread").html(generateChat(response.messages))
            $("#conversation-thread").get(0).scrollTo(0, $("#conversation-thread").get(0).scrollHeight);
        }else{
            window.location.href = "http://localhost:8000/auth/login";
        }
    })
}

//adding listeners to switch chats
$("div.conversation").each((index,element) => {
    let div = $(element) // back to JQuery object
    //get first p child, which is chat name, and making it into a JQuery object again
    let child = $(div.children("p:first-child").get())
    //add loading upon clicking
    div.on('click',() => loadChat(child.html()))
})

//adding listeners to send messages
$($("#writing-area").children("form")).on('submit', (event) => {
    console.log("fooled");
    event.preventDefault();
    sendMessage($("#conversation-title h3").html(), $("#new-message").val())
    $("#new-message").val("")
})

setInterval(() => {loadChat($("#conversation-title h3").html())}, 2500)
*/
var container = $("#conversation-thread");
setInterval(function() {
    $.ajax({
       type: 'GET',
        url: '/get_messages/',
        success: function(response) {
            var lastMessage = container.children().last();
            container.scrollTop(container.prop("scrollHeight"));
        }
    });
}, 2500);
 