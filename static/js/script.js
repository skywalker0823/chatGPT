// When DOM ready
document.addEventListener('DOMContentLoaded', () => {
    //say hello
    document.getElementById("loading").style.display = "none";
    console.log('Hello World!');
});


send = async () => {
    // clear the response and display loading image
    // document.getElementById("response").innerHTML = "";
    document.getElementById("loading").style.display = "block";
    const message = document.getElementById('message').value;
    // display my message,starts with Me, not using innseHTML
    const my_message = document.createElement('div');
    my_message.className = "my_message";
    my_message.innerHTML = message;
    document.getElementById("response").appendChild(my_message);


    
    const response = await fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message_log : message
        })
    });
    const data = await response.json();
    console.log(data);
    document.getElementById("loading").style.display = "none";
    // document.getElementById("response").innerHTML = data;
    // display chatbot message
    const chatbot_message = document.createElement('div');
    chatbot_message.className = "chatbot_message";
    chatbot_message.innerHTML = data;
    document.getElementById("response").appendChild(chatbot_message);

}

// document.getElementById("clear_button").addEventListener("click", () => {
//     document.getElementById("message").value = "";
//     document.getElementById("response").innerHTML = "";
// });