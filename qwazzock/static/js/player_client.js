$(document).ready(function () {
    $("#buzzer").click(function () {
        console.log("Buzzer buzzed via POST.");
        $.post('https://' + document.domain + ':' + location.port + '/buzz', { name: $("#name").val()});
    });
});
