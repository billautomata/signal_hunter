var zmq = require('zmq')
var xmlrpc = require('xmlrpc')
var buffer_utils = require('./lib/BufferUtils.js')

var xmlrpc_client = xmlrpc.createClient({
  host: 'localhost',
  port: 8080,
  path: '/'
})

var constants = require('./lib/constants.js')
var FFT_BUFFER_LENGTH = constants.FFT_SIZE * constants.FLOAT32_SIZE

var sock = zmq.socket('pull')
var sock_iqs = zmq.socket('pull')

sock.connect('tcp://127.0.0.1:9000');
sock_iqs.connect('tcp://127.0.0.1:9001')

var count = 0

sock.on('message', function(msg){
  count += 1
  if(count % 10 === 0){
    var buffers = []
    var buffer_index = 0
    while(buffer_index < msg.length){
      buffers.push(msg.slice(buffer_index,buffer_index+FFT_BUFFER_LENGTH))
      buffer_index += FFT_BUFFER_LENGTH
    }

    buffers.forEach(function(msg){
      var stats = buffer_utils.find_peak(msg)
      // console.log(stats)
      buffer_utils.draw_buffer(msg, stats.average)
    })

    // // console.log('max', max)
    // var freq = 91500000 + (count*100)
    // xmlrpc_client.methodCall('set_frequency', [ freq ], function(err, value){
    //   // console.log('set frequency ', value)
    //   if(err){
    //     console.log('error',err)
    //   }
    // })
  }
});

sock_iqs.on('message', function(message){
  // console.log('iq msg', message.length)
})
