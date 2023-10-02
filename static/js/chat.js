const lastMessageCreatedAt = "{{ lastMessage.created_at }}";
const lastMessageText = "{{ lastMessage.text }}";

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
    let currentDate = getCurrentDate();
    displayPendingMessage(currentDate);

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
        console.log('Fehler', e);
    }
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


function getCurrentDate() {
    return new Date().toLocaleDateString('de-DE');
}


function displayPendingMessage(date) {
    messageContainer.innerHTML += `
    <div id="deleteMessage">
      <span class="grey"> [${date}]</span> ${window.currentUser}: <span class="grey"> ${messageField.value} </span>
    </div>`;
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
    document.getElementById('deleteMessage').remove();

    let rawDate = dataAsJson.created_at;
    let parts = rawDate.split('-');
    let formattedDate = `${parts[2]}.${parts[1]}.${parts[0]}`;

    messageContainer.innerHTML += `
      <div>
        <span class="grey"> [${formattedDate}]</span>${dataAsJson.author}: <span> ${dataAsJson.text} </span>
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
    console.log(receiver);
    fd.append('csrfmiddlewaretoken', token);
    fd.append('receiver_id', receiver);

    let response = await fetch('/chat/', {
        method: 'POST',
        body: fd
    });

    try{
        if(response.ok){
            console.log('empfänger:',receiver);
            window.location.href = '/chat/?receiver_id=' + receiver;
        } else {
            let data = await response.json();
            alert(data.message); 
            console.log('Failed to send message back', data.error);
        }
    }
    catch(e){
        console.error("Error during fetch:", e);
    }
}
