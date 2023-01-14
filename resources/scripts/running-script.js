username = $('#username').html()
if(username != ""){
    console.log(username)
}else{
    console.log("no username")
}

function generateChat(messages){
    str = ""
    for(message of messages){
        str += "<li>\n"
        if(message.author.username == username){
            str += "<div class=\"message-me\">\n"
        }else{
            str += "<div class=\"message-other\">\n"
        }
        str += "<p>" + message.author.username + "</p>\n"
        str += "<p>" + message.content + "</p>\n"
        str += "<p>" + message.publication_date + "</p>\n"
        str += "</div>\n"
        str += "</li>\n"
    }
    return str
}

function loadChat(chatname){
    $.ajax('http://localhost:8000/chat/getMessages', {
        method:'GET',
        data: {
            "chatName":chatname,
        },
    }).done( response => {
        console.log(response)
        $("#conversation-thread").html(generateChat(response.messages))
    })
}

loadChat("general")



