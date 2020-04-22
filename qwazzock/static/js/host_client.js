$(document).ready(function () {
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/host_client_socket');
    socket.on('host_client_data', function (msg) {
        $('#player').html("Player in hotseat: " + msg.player_in_hotseat);
        $('#team').html("Team in hotseat: " + msg.team_in_hotseat);
    });
});

$(document).ready(function () {
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/host_client_socket');
    $("#pass").click(function () {
        socket.emit('pass');
    });
});
