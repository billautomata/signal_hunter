var constants = require('./constants.js')
var d3 = require('d3')

module.exports.find_peak = find_peak
module.exports.draw_buffer = draw_buffer
module.exports.histogram = histogram
module.exports.float_array = float_array

function float_array(buffer){
  var a = []
  for(var i= 0; i < buffer.length; i+=constants.FLOAT32_SIZE){
    var v = buffer.readFloatLE(i)
    a.push(v)
  }
  return a
}

function find_peak(buffer){
  var min = 1024.0  // dummy value
  var max = 0
  var median = 0
  var sum = 0
  var average = 0

  var max = 0
  var a = []

  for(var i= 0; i < buffer.length; i+=constants.FLOAT32_SIZE){
    var v = buffer.readFloatLE(i)
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

function draw_buffer(buffer, limit){
  for(var i= 0; i < buffer.length; i+=(constants.FLOAT32_SIZE*5)){
    var v = buffer.readFloatLE(i)
    if(v < limit){
      process.stdout.write('-')
    } else {
      process.stdout.write('*')
    }
  }

  var stats = find_peak(buffer)
  process.stdout.write(' ' + String(stats.median.toFixed(2)))
  process.stdout.write('\n')
}

function histogram(buffer){
  var domain = [-3.0, 3.0]
  var n_buckets = 100
  var buckets = []
  var scale_value_to_bucket_index = d3.scaleQuantile()
    .domain(domain).range(d3.range(0,n_buckets,1))

  for(var i = 0; i < n_buckets; i++){
    buckets.push(0)
  }
  for(var i= 0; i < buffer.length; i+=constants.FLOAT32_SIZE){
    var v = buffer.readFloatLE(i)
    var idx = scale_value_to_bucket_index(v)
    // console.log('buffer value', v, 'mapped index', idx)
    buckets[idx] += 1
  }
  console.log(JSON.stringify(buckets))
}
