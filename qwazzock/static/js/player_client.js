$(document).ready(function () {
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/player_client_socket');
    $("#buzzer").click(function () {
        console.log("Buzzer buzzed via POST.");
        socket.emit('buzz', { player_name: $("#player_name").val(), team_name: $("#team_name").val() })
    });
});
