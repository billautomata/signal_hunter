var zmq = require('zmq')
var xmlrpc = require('xmlrpc')

var xmlrpc_client = xmlrpc.createClient({
  host: 'localhost',
  port: 8080,
  path: '/'
})


var sock = zmq.socket('pull')
var sock_iqs = zmq.socket('pull')

sock.connect('tcp://127.0.0.1:9000');
sock_iqs.connect('tcp://127.0.0.1:9001')



var count = 0

sock.on('message', function(msg){
  count += 1
  if(count % 100 === 0){
    // console.log(msg)
    var max = 0
    for(var i= 0; i < msg.length; i+=4){
      var v = Math.abs(msg.readFloatLE(i))
      // console.log((i/4),v.toFixed(8))
      // var v = msg.readFloatLE(i)
      if(v > max){
        max = v
      }
    }
    console.log('max', max)
    var freq = 91500000 + count
    xmlrpc_client.methodCall('set_frequency', [ freq ], function(err, value){
      console.log('set frequency ', value)
      if(err){
        console.log('error',err)
      }
    })
  }
  // console.log('work: %s', msg.length);
});

sock_iqs.on('message', function(message){
  console.log('iq msg', message.length)
})
