var constants = require('./constants.js')
var d3 = require('d3')

module.exports.analyze = analyze
module.exports.draw_buffer = draw_buffer
module.exports.find_histogram = find_histogram
module.exports.float_array = float_array
module.exports.find_peaks = find_peaks

function float_array(buffer){
  var a = []
  for(var i= 0; i < buffer.length; i+=constants.FLOAT32_SIZE){
    var v = buffer.readFloatLE(i)
    a.push(v)
  }
  return a
}

function analyze(buffer){
  var min = 1024.0  // dummy value
  var max = 0
  var median = 0
  var sum = 0
  var average = 0

  var max = 0
  var a = []

  for(var i= 0; i < buffer.length; i+=constants.FLOAT32_SIZE){
    var v = buffer.readFloatLE(i)
    if(v < 0){
      v = 0
    }
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

function draw_buffer(buffer, limit, step){
  if(step === undefined){
    step = 4
  }
  for(var i= 0; i < buffer.length; i+=(constants.FLOAT32_SIZE*step)){
    var found = false
    for(var j = 0; j < step; j++){
      var idx = i+(j*constants.FLOAT32_SIZE)
      if(idx < buffer.length){
        var v = buffer.readFloatLE(i+(j*constants.FLOAT32_SIZE))
        if(v > limit){
          found = true
        }
      }
    }
    if(!found){
      process.stdout.write('-')
    } else {
      process.stdout.write('*')
    }
  }

  var stats = analyze(buffer)
  process.stdout.write(' ' + String(stats.min.toFixed(2)))
  process.stdout.write('\n')
}

function find_histogram(buffer, domain, n_buckets){
  var buckets = []

  if(domain === undefined){
    domain = [-5.0, 5.0]
  }
  if(n_buckets === undefined){
    n_buckets = 100
  }

  var scale_value_to_bucket_index = d3.scaleQuantile()
    .domain(domain).range(d3.range(0,n_buckets,1))

  for(var i = 0; i < n_buckets; i++){
    buckets.push(0)
  }

  for(var i= 0; i < buffer.length; i+=constants.FLOAT32_SIZE){
    var v = buffer.readFloatLE(i)
    var idx = scale_value_to_bucket_index(v)
    buckets[idx] += 1
  }
  return buckets
}

function find_peaks(buffer, threshold){

  if(threshold === undefined){
    threshold = 0.3
  }

  // get stats
  var stats = analyze(buffer)
  // get histogram
  var n_buckets = 100
  var domain = [ stats.min, stats.max ]
  var histogram = find_histogram(buffer, domain, n_buckets)

  var scale_value_to_bucket_index = d3.scaleQuantile()
    .domain(domain).range(d3.range(0,n_buckets,1))

  var max_histogram_value = 0
  var max_histogram_idx = 0
  histogram.forEach(function(v,idx){
    if(v > max_histogram_value) {
      max_histogram_value = v
      max_histogram_idx = idx
    }
  })

  var most_common_value = scale_value_to_bucket_index.invertExtent(max_histogram_idx)

  // draw_buffer(buffer, most_common_value[0]+threshold)

  // build peaks
  var a = []
  for(var i = 0; i < buffer.length; i += constants.FLOAT32_SIZE){
    var v = buffer.readFloatLE(i)
    v = Math.abs(v)
    if(v > most_common_value[0]+threshold){
      a.push(1)
    } else {
      a.push(0)
    }
  }

  return a

}
