$(document).ready(function () {
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/player_client_socket');
    socket.on('player_client_data', function (msg) {
        if (msg.player_in_hotseat == $("#player_name").val()) {
            $("#feedback").html(msg.player_in_hotseat + ", you are in the hotseat!")
            $("#buzzer").prop("disabled", true);
        } else if (msg.player_in_hotseat != "Pending") {
            $("#feedback").html(msg.player_in_hotseat + " (" + msg.team_in_hotseat + ") is in the hotseat.")
            $("#buzzer").prop("disabled", true);
        } else if (jQuery.inArray($("#team_name").val(), msg.locked_out_teams) !== -1) {
            $("#feedback").html("Your team is locked out.")
            $("#buzzer").prop("disabled", true);
        } else {
            $("#feedback").html("Fingers on buzzers!")
            $("#buzzer").prop("disabled", false);
        }
    });
    $("#buzzer").click(function () {
        if ($("#player_name").val().trim() == "") {
            $("#feedback").html("Player name cannot be blank.")
        } else if ($("#team_name").val().trim() == "") {
            $("#feedback").html("Team name cannot be blank.")
        } else {
            console.log("Buzzer buzzed.");
            socket.emit('buzz', { player_name: $("#player_name").val(), team_name: $("#team_name").val() })
        }
    });
});
