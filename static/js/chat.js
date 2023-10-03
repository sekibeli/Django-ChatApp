const lastMessageCreatedAt = "{{ lastMessage.created_at }}";
const lastMessageText = "{{ lastMessage.text }}";


// document.addEventListener("DOMContentLoaded", function() {
//     const sendButton = document.getElementById("sendButton");
//     const messageField = document.getElementById("messageField");
    
//     messageField.addEventListener("input", function() {
//         if (this.value.length >= 2) {
//             sendButton.style.display = "inline-block";  // Button anzeigen
//         } else {
//             sendButton.style.display = "none";  // Button verstecken
//         }
//     });
// });



function getReceiverIdFromUrl() {
    let params = new URLSearchParams(window.location.search);
    return params.get('receiver_id');
}

/**
 * Sends a message to the server and updates the message container on success.
 * @async
 * @function
 * @throws Will log an error to the console if there's an issue during the request.
 */
async function sendMessage() {
    let fd = constructFormData();
    // let currentDate = getCurrentDate();
    let currentTime = getCurrentTime();
    displayPendingMessage(currentTime);

    try {
        let response = await fetchDataToServer(fd);

        if (response.ok) {
            let data = await response.json();
            handleServerResponse(data);
            messageField.value = '';
        } else {
            console.log('Failed to send message back');
        }
    } catch (e) {
        // console.log('Fehler', e);
    }
    let messageContainer = document.getElementById('messageContainer');
    messageContainer.scrollTop = messageContainer.scrollHeight;
}

/**
 * Constructs a FormData object containing CSRF token, message text, and receiver ID.
 * @function
 * @returns {FormData} A FormData object with necessary data for chat messages.
 */
function constructFormData() {
    let fd = new FormData();
    let token = document.getElementById('csrfToken').value;
    let receiverId = getReceiverIdFromUrl();
    fd.append('csrfmiddlewaretoken', token);
    fd.append('textmessage', messageField.value);
    fd.append('receiver_id', receiverId);
    return fd;
}


// function getCurrentDate() {
//     return new Date().toLocaleDateString('de-DE');
// }

function getCurrentTime(){
           return new Date().toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' });
    }


function displayPendingMessage(time) {
    if (messageField.value.length > 2){
    messageContainer.innerHTML += `
    <div id="deleteMessage">
         <div class="clearfix">
             <div class="flipped background_author">
                 <div>${messageField.value}</div>
                 <div class="time">${time}<img class="tick" src="../static/img/tick_grey.png"></div>
             </div>
        </div>
    </div>`;

    }
}


async function fetchDataToServer(fd) {
    return await fetch('/chat/', {
        method: 'POST',
        body: fd
    });
}

/**
 * Handles the server's response after sending a chat message.
 * Parses the provided data, removes the pending message indicator, and appends the 
 * actual message to the chat container with the formatted date.
 * 
 * @function
 * @param {Array} data - The server's response data, which contains details about the sent message.
 */
function handleServerResponse(data) {
    let dataAsJson = data[0]['fields'];
    console.log('1', dataAsJson);
    document.getElementById('deleteMessage').remove();

    // let rawDate = dataAsJson.created_at;
   time = dataAsJson['time_created'].substring(0, 5);
    // let parts = rawDate.split('-');
    // let formattedDate = `${parts[2]}.${parts[1]}.${parts[0]}`;
// console.log('2,', dataAsJson);
    messageContainer.innerHTML += `
    <div class="clearfix">
    <div class="flipped background_author">
        <div>${messageField.value}</div>
        <div class="time">${time}<img class="tick" src="../static/img/doubleTick.png"></div>
  </div>
</div>`;
    
   
}


async function login() {
    let fd = new FormData();
    let token = document.getElementById('csrfTokenLogin').value;
    fd.append('csrfmiddlewaretoken', token);
    fd.append('username', username.value);
    fd.append('password', password.value);
    fd.append('redirect', document.querySelector('input[name="redirect"]').value)


    let response = await fetch('/login/', {
        method: 'POST',
        body: fd
    });

    try {
        if (response.ok) {
            window.location.href = '/overview';
        } else {
            let data = await response.json();
            alert(data.message); 
            console.log('Failed to send message back', data.error);

        }


    } catch (e) {
        console.log('Fehler', e)
    }
}

async function signin(){
    let fd = new FormData();
    let token = document.getElementById('csrfTokenSignin').value;
    console.log(token);
    fd.append('csrfmiddlewaretoken', token);
    fd.append('username', username.value);
    fd.append('email', email.value);
    fd.append('password', password.value);
    fd.append('repeat_password', repeat_password.value);

    let response = await fetch('/signin/', {
        method: 'POST',
        body: fd
    });

    try{
        if(response.ok){
            window.location.href = '/login'
        } else {
            let data = await response.json();
            alert(data.message); 
            console.log('Failed to send message back', data.error);
        }
    }
    catch(e){}
}

async function chooseChat(receiver){
    let fd = new FormData();
    let token = document.getElementById('csrfTokenChoose').value;
    console.log('receiver:', receiver);
    fd.append('csrfmiddlewaretoken', token);
    fd.append('receiver_id', receiver);

    console.log('chooseChat:',receiver);
   
        let response = await fetch('/chat/', {
        method: 'POST',
        body: fd
    });


        if(response.ok){
            console.log('Response Status:', response.status, 'Response Status Text:', response.statusText);
            console.log('empfänger:',receiver);
            window.location.href = '/chat/?receiver_id=' + receiver;
        } else {
            console.error('Response Status:', response.status, 'Response Status Text:', response.statusText);
            let data = await response.json();
            alert(data.message); 
            console.log('Failed to send message back', data.error);
          
        }
       
    
   
}

