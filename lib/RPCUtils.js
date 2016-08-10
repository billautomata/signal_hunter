var xmlrpc = require('xmlrpc')

module.exports = function(){

  var xmlrpc_client = xmlrpc.createClient({
    host: 'localhost',
    port: 8080,
    path: '/'
  })

  function set_frequency(v){
    var freq = v
    xmlrpc_client.methodCall('set_frequency', [ freq ], function(err, value){
      // console.log('set frequency ', value)
      if(err){
        console.log('error setting frequency',err)
      }
    })
  }

  function get(key, cb){
    xmlrpc_client.methodCall('get_'+key, [], function(err, value){
      if(err){
        console.log('error setting value',err, key)
      } else {
        cb(value)
      }
    })
  }

  function set(key, value){
    xmlrpc_client.methodCall('set_'+key, [ value ], function(err){
      if(err){
        console.log('error setting frequency',err)
      } else {
        // console.log(key, ' set to ', value)
      }
    })
  }

  return {
    set_frequency: set_frequency,
    set: set,
    get: get
  }

}
