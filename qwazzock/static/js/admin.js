$(document).ready(function () {
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/buzz_data_socket');
    socket.on('buzz_data', function (msg) {
        $('#log').html("Player in hotseat: " + msg.player_in_hotseat);
    });
});

$(document).ready(function () {
    var socket = io.connect('https://' + document.domain + ':' + location.port + '/pass_socket');
    $("#pass").click(function () {
        socket.emit('pass');
        // $('#log').html("Player in hotseat: Pending");
    });
});
