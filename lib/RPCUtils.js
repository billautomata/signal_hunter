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
