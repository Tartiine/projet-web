$.ajax('http://localhost:8000/chat/getMessages', {
    method:'GET',
    body:{
        "chatName":'general',
    }
}).done( response => {
    console.log("response gotten")
    console.log(response.messages)
})