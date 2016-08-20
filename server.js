var buffer_utils = require('./lib/BufferUtils.js')
var constants = require('./lib/constants.js')
var fs = require('fs')
var Buffer = require('buffer').Buffer
var express = require('express')
var http = require('http')
var socket_io = require('socket.io')

var zmq = require('zmq')

var sock_fft = zmq.socket('pull')
var sock_iqs = zmq.socket('pull')

sock_fft.connect('tcp://127.0.0.1:9000');
sock_iqs.connect('tcp://127.0.0.1:9001')

var io
var sockets = []

var app = express()
var server = http.createServer(app).listen(8000, function(){
  io = socket_io(server)
  io.on('connection', function(socket){
    console.log('a user connected');

    sockets.push(socket)
    console.log(sockets.length, 'users total')
    socket.on('disconnect', function(){
      sockets = sockets.filter(function(s){ return s !== socket })
    })

    hunter.rpc_update(function(v){
      socket.emit('radio_data', v)
    })

    socket.on('get_frequency', function(msg){

    })
  })
})

app.use(express.static(__dirname + '/public'))

var FFT_BUFFER_LENGTH = constants.FFT_SIZE * constants.FLOAT32_SIZE

var hunter = require('./lib/SignalHunter.js')({
  frequency: 930000000
})

var count = 0

sock_fft.on('message', function(msg){
  count += 1
  if(count % 100 === 0){
    // split the buffers
    var buffers = []
    var buffer_index = 0
    while(buffer_index < msg.length){
      buffers.push(msg.slice(buffer_index,buffer_index+FFT_BUFFER_LENGTH))
      buffer_index += FFT_BUFFER_LENGTH
    }
    // draw each buffer
    buffers.forEach(function(msg){
      sockets.forEach(function(socket){
        socket.emit('fft_data', buffer_utils.float_array(msg))
      })
      // var stats = buffer_utils.analyze(msg)
      // buffer_utils.draw_buffer(msg, 0.25)
      // buffer_utils.find_histogram(msg)
      var peaks = buffer_utils.find_peaks(msg)
      hunter.tick(peaks)
    })
  }
})

sock_iqs.on('message', function(message){
  hunter.iq_packet(message)
})
