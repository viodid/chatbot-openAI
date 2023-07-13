// Codepen: https://codepen.io/zenworm/pen/KqLNPm
const $ChatInput = $('.ChatInput-input');
const $NewChat = $('.new-chat');


$NewChat.click(function () {
  window.location.href = '/refresh';
});

$ChatInput.keyup(function (e) {
  if (e.shiftKey && (e.which === 13)) {
    e.preventDefault();
    return false;
  }
  const currentDate = new Date();
  const currentTime = currentDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  const $this = $(this);
  if (e.which === 13) {
    const newText = $this.html();
    send_message(newText.split('<div>')[0]);
    $this.html('');
    $('.ChatWindow').append(`\
    <div class="ChatItem ChatItem--expert"> \
    <div class="ChatItem-meta"> \
    <div class="ChatItem-avatar"> \
    <img class="ChatItem-avatarImage" src="static/img/tck.png"> \
    </div> \
    </div> \
    <div class="ChatItem-chatContent"> \
    <div class="ChatItem-chatText">` + newText + `</div> \
    <div class="ChatItem-timeStamp"><strong>Me</strong> · Today ${currentTime}</div> \
    </div> \
    </div>\
  `);
    return $('.ChatWindow').animate({ scrollTop: $('.ChatWindow').prop("scrollHeight") }, 500);
  }
});

function ai_answer(message) {
  const currentDate = new Date();
  const currentTime = currentDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  $('.ChatWindow').append(`
    <div class="ChatItem ChatItem--user">
      <div class="ChatItem-meta">
        <div class="ChatItem-avatar">
          <img class="ChatItem-avatarImage" src="static/img/openai.png">
        </div>
      </div>
      <div class="ChatItem-chatContent">
        <div class="ChatItem-chatText">${message}</div>
        <div class="ChatItem-timeStamp"><strong>Chat Bot</strong> · Today ${currentTime}</div>
      </div>
    </div>
  `);

  return $('.ChatWindow').animate({ scrollTop: $('.ChatWindow').prop("scrollHeight") }, 500);
}


// WebSockets: https://socket.io/docs/v4/client-socket-instance/
var socket = io();

socket.on('ai_answer', data => {
  ai_answer(data);
});

function send_message(message) {
  socket.emit('messages', { data: message });
}