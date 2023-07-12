const $ChatInput = $('.ChatInput-input');

$ChatInput.keyup(function (e) {
  if (e.shiftKey && (e.which === 13)) {
    e.preventDefault();
    return false;
  }
  const $this = $(this);
  if (e.which === 13) {
    const newText = $this.html();
    $this.html('');
    $('.ChatWindow').append(`\
<div class="ChatItem ChatItem--expert"> \
<div class="ChatItem-meta"> \
<div class="ChatItem-avatar"> \
<img class="ChatItem-avatarImage" src="https://randomuser.me/api/portraits/women/0.jpg"> \
</div> \
</div> \
<div class="ChatItem-chatContent"> \
<div class="ChatItem-chatText">` + newText + `</div> \
<div class="ChatItem-timeStamp"><strong>Me</strong> · Today 05:49</div> \
</div> \
</div>\
`);
    return $('.ChatWindow').animate({ scrollTop: $('.ChatWindow').prop("scrollHeight") }, 500);
  }
});