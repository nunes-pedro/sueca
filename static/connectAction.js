var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function () {
    console.log('Connected')
    //socket.emit('message', { data: 'Im Here' })
});
socket.on('s2c_msg', function (msg) {
    console.log(msg)
});

