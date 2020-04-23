$(document).ready(function () {
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/host_client_socket');
    socket.on('host_client_data', function (msg) {
        $('#player').html("Player in hotseat: " + msg.player_in_hotseat);
        $('#team').html("Team in hotseat: " + msg.team_in_hotseat);
        $('#locked_out').html("Locked out: " + msg.locked_out_teams);
        $('#scores').html("Scores: " + JSON.stringify(msg.scores));
        if (msg.player_in_hotseat == "Pending") {
            $("#right").prop("disabled", true);
            $("#wrong").prop("disabled", true);
        } else {
            $("#right").prop("disabled", false);
            $("#wrong").prop("disabled", false);
        }
    });
    $("#pass").click(function () {
        socket.emit('pass');
    });
    $("#right").click(function () {
        socket.emit('right');
    });
    $("#wrong").click(function () {
        socket.emit('wrong');
    });
});