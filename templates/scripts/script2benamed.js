$(document).ready(function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function () {
        socket.emit('sweetroom', { data: 'Im Here' })
    });

    socket.on('c2server')

});