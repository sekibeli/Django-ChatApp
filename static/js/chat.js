const lastMessageCreatedAt = "{{ lastMessage.created_at }}";
  const lastMessageText = "{{ lastMessage.text }}";

  async function sendMessage() {
    let fd = new FormData();
    let token = document.getElementById('csrfToken').value;
    // let token = '{{csrf_token}}';
    console.log(token);
    fd.append('csrfmiddlewaretoken', token);
    fd.append('textmessage', messageField.value);
   

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
        let data = await response.json();
        let dataAsJson = JSON.parse(data);
        dataAsJson = dataAsJson['fields'];
        document.getElementById('deleteMessage').remove();
        console.log('json:', dataAsJson);
        let rawDate = dataAsJson.created_at;   // z.B. "2023-09-29"
        let parts = rawDate.split('-');       // Teilt den String in ein Array: ["2023", "09", "29"]
        let formattedDate = `${parts[2]}.${parts[1]}.${parts[0]}`;  // Erzeugt den gewünschten Format: "29.09.2023"

        messageContainer.innerHTML += `
      <div>
        <span class="grey"> [${formattedDate}]</span>${window.currentUser}: <span> ${dataAsJson.text} </span>
      </div>`;
        messageField.value = '';
      } else {
        console.log('Failed to send message back');
      }


    } catch (e) {
      console.log('Fehler', e)
    }
  }
