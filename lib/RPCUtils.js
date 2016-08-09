var xmlrpc = require('xmlrpc')

var xmlrpc_client = xmlrpc.createClient({
  host: 'localhost',
  port: 8080,
  path: '/'
})

module.exports.set_frequency = function set_frequency(v){
  var freq = v
  xmlrpc_client.methodCall('set_frequency', [ freq ], function(err, value){
    // console.log('set frequency ', value)
    if(err){
      console.log('error setting frequency',err)
    }
  })
}

module.exports.get = function get(key, cb){
  xmlrpc_client.methodCall('get_'+key, [], function(err, value){
    if(err){
      console.log('error setting frequency',err)
    } else {
      cb(value)
    }
  })
}

module.exports.set = function set(key, value){
  xmlrpc_client.methodCall('get_'+key, [ value ], function(err){
    if(err){
      console.log('error setting frequency',err)
    } else {
      console.log(key, 'set to', value)
    }
  })
}
