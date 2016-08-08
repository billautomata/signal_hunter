var constants = require('./constants.js')

module.exports.find_peak = function find_peak(buffer){
  var min = 1024.0  // dummy value
  var max = 0
  var mean = 0
  var sum = 0
  var average = 0

  var max = 0
  for(var i= 0; i < buffer.length; i+=constants.FLOAT32_SIZE){
    var v = Math.abs(buffer.readFloatLE(i))
    sum += v

    if(v > max){
      max = v
    }
    if(v < min){
      min = v
    }

  }
  return {
    max: max,
    min: min,
    average: (sum/buffer.length)
  }
}

module.exports.draw_buffer = function draw_buffer(buffer, limit){
  for(var i= 0; i < buffer.length; i+=(constants.FLOAT32_SIZE*5)){
    var v = Math.abs(buffer.readFloatLE(i))
    if(v < limit){
      process.stdout.write('-')
    } else {
      process.stdout.write('*')
    }
  }
  process.stdout.write('\n')
}
