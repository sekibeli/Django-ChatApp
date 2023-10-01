const lastMessageCreatedAt = "{{ lastMessage.created_at }}";
const lastMessageText = "{{ lastMessage.text }}";

function getReceiverIdFromUrl() {
    let params = new URLSearchParams(window.location.search);
    return params.get('receiver_id');
}

async function sendMessage() {
    let fd = new FormData();
    let token = document.getElementById('csrfToken').value;
    // let token = '{{csrf_token}}';
    console.log(token);
    let receiverId = getReceiverIdFromUrl();
    fd.append('csrfmiddlewaretoken', token);
    fd.append('textmessage', messageField.value);
    fd.append('receiver_id', receiverId);


    try {
        const currentDate = new Date().toLocaleDateString('de-DE');

        messageContainer.innerHTML += `
    <div id="deleteMessage">
      <span class="grey"> [${currentDate}]</span> ${window.currentUser}: <span class="grey"> ${messageField.value} </span>
    </div>`;

        let response = await fetch('/chat/', {
            method: 'POST',
            body: fd
        });

        if (response.ok) {
            let dataAsJson;
            let data = await response.json();
            dataAsJson = data[0]['fields'];
            document.getElementById('deleteMessage').remove();
            let rawDate = dataAsJson.created_at;   // z.B. "2023-09-29"
            let parts = rawDate.split('-');       // Teilt den String in ein Array: ["2023", "09", "29"]
            let formattedDate = `${parts[2]}.${parts[1]}.${parts[0]}`;  // Erzeugt den gewünschten Format: "29.09.2023"

            messageContainer.innerHTML += `
      <div>
        <span class="grey"> [${formattedDate}]</span>${dataAsJson.author}: <span> ${dataAsJson.text} </span>
      </div>`;
            messageField.value = '';
        } else {
            console.log('Failed to send message back');
        }


    } catch (e) {
        console.log('Fehler', e)
    }
}


async function login() {
    let fd = new FormData();
    let token = document.getElementById('csrfTokenLogin').value;
    // let token = '{{csrf_token}}';
    console.log(token);
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
