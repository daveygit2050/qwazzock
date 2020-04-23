$(document).ready(function () {
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/player_client_socket');
    socket.on('player_client_data', function (msg) {
        if (msg.player_in_hotseat != "Pending" || jQuery.inArray($("#team_name").val(), msg.locked_out_teams) !== -1) {
            $("#buzzer").prop("disabled", true);
        } else {
            $("#buzzer").prop("disabled", false);
        }
    });
    $("#buzzer").click(function () {
        console.log("Buzzer buzzed via POST.");
        socket.emit('buzz', { player_name: $("#player_name").val(), team_name: $("#team_name").val() })
    });
});
