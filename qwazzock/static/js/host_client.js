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
        $('#teams').html("Teams: ");
        $.each(msg.scores, function (team_name, team_score) {
            var state = "enabled";
            if (jQuery.inArray(team_name, msg.locked_out_teams) !== -1){
                state = "disabled";
            };
            $('#teams').append(`<button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" id="team-${team_name}" style="height:5vh;margin-right:1vw;" ${state}>${team_name} (${team_score})</button>`);
            $(`#team-${team_name}`).click(function () {
                socket.emit('team', { team_name: team_name });
            });
        });
        if (msg.player_in_hotseat == "Pending") {
            $("#right").prop("disabled", true);
            $("#wrong").prop("disabled", true);
        } else {
            buzzerAudio.play();
            $("#right").prop("disabled", false);
            $("#wrong").prop("disabled", false);
        }
        if (msg.question_type == "standard") {
            $("#standard").prop("disabled", true);
            $("#picture").prop("disabled", false);
            $("#answer").html("")
        } else {
            $("#standard").prop("disabled", false);
            $("#picture").prop("disabled", true);
            $("#answer").html("Question Image: " + msg.selected_image)
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
        var wrong_answer_penalty = $("#wrong_answer_penalty").val();
        socket.emit('wrong', { wrong_answer_penalty: wrong_answer_penalty });
    });
    $("#standard").click(function () {
        console.log("Switching to standard question type.")
        socket.emit('standard');
    });
    $("#picture").click(function () {
        console.log("Switching to picture question type.")
        socket.emit('picture');
    });

    var dialogButton = document.querySelector('#reset-button');
    dialogButton.addEventListener('click', function() {
       dialog.showModal();
    });
    dialog.querySelector('button.dialog-cancel').addEventListener('click', function() {
      dialog.close();
    });

});