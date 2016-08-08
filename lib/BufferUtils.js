var constants = require('./constants.js')

module.exports.find_peak = function find_peak(buffer){
  var min = 1024.0  // dummy value
  var max = 0
  var median = 0
  var sum = 0
  var average = 0

  var max = 0
  var a = []

  for(var i= 0; i < buffer.length; i+=constants.FLOAT32_SIZE){
    var v = Math.abs(buffer.readFloatLE(i))
    a.push(v)
    sum += v

    if(v > max){
      max = v
    }
    if(v < min){
      min = v
    }
  }
  a = a.sort()
  median = a[Math.floor(a.length*0.5)]
  return {
    max: max,
    min: min,
    average: (sum/buffer.length),
    median: median
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
