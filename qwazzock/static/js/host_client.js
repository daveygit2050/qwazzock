$(document).ready(function () {

    var buzzerAudio = document.createElement('audio');
    buzzerAudio.setAttribute('src', '/static/audio/meh.mp3');

    var dialog = document.querySelector('#reset-dialog');
    if (! dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }

    var socket = io.connect(document.location.origin + '/host_client_socket');
    socket.on('host_client_data', function (msg) {
        $('#player').html("Player in hotseat: " + msg.player_in_hotseat);
        $('#team').html("Team in hotseat: " + msg.team_in_hotseat);
        $('#locked_out').html("Locked out: " + msg.locked_out_teams);
        $('#scores').html("Scores: " + JSON.stringify(msg.scores));
        if (msg.player_in_hotseat == "Pending") {
            $("#right").prop("disabled", true);
            $("#wrong").prop("disabled", true);
        } else {
            buzzerAudio.play();
            $("#right").prop("disabled", false);
            $("#wrong").prop("disabled", false);
        }
    });

    $("#pass").click(function () {
        socket.emit('pass');
    });
    $("#reset-confirm").click(function () {
        socket.emit('reset');
        dialog.close();
    });
    $("#right").click(function () {
        var score_value = $("#score_value").val();
        socket.emit('right', { score_value: score_value });
    });
    $("#wrong").click(function () {
        socket.emit('wrong');
    });

    var dialogButton = document.querySelector('#reset-button');
    dialogButton.addEventListener('click', function() {
       dialog.showModal();
    });
    dialog.querySelector('button.dialog-cancel').addEventListener('click', function() {
      dialog.close();
    });

});