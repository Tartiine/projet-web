user = $("username")

function generateChat(messages){

}



$.ajax('http://localhost:8000/chat/getMessages', {
    method:'GET',
    data: {
        "chatName":'general',
    },
}).done( response => {
    console.log("response gotten")
    console.log(response.messages)
})