var d3 = require('d3')
var rpc = require('./RPCUtils.js')()
var recorder = require('./IQRecorder.js')()
var async = require('async')

module.exports = function SignalHunter(options){

  // options.frequency
  // options.sample_rate
  // options.fft_size

  if(options === undefined){
    options = {}
  }

  if(options.frequency === undefined){
    options.frequency = 929000000
  }
  if(options.sample_rate === undefined){
    options.sample_rate = 2000000
  }
  if(options.bandwidth === undefined){
    options.bandwidth = 2000000
  }
  if(options.fft_size === undefined){
    options.fft_size = 2048
  }

  var frequency = options.frequency

  var samp_rate
  var offset_frequency

  var count_at_this_frequency = 0
  var limit = 100

  var scale_index_to_frequency = d3.scaleLinear()
    .domain([0, options.fft_size])
    .range([frequency-(options.bandwidth*0.5), frequency+(options.bandwidth*0.5)])

  var identified_signals = []
  var new_signals = []
  var previous_peaks = []
  var current_peaks = []

  var current_identified_frequencies = []
  var current_identified_frequency_indexes = []

  var hunter_freq_0 = 0

  var running_identified_indexes = []

  //
  rpc.set('frequency', frequency)

  for(var i = 0; i < options.fft_size; i++){
    identified_signals.push(0)
    new_signals.push(0)
    previous_peaks.push(0)
    current_peaks.push(0)
    running_identified_indexes.push(0)
  }

  ////////////////////////////////////////////////////////////////////////////
  ////////////////////////////////////////////////////////////////////////////
  function tick(new_peaks){

    // identify new signals using a ping pong method
    previous_peaks.forEach(function(v,idx){
      previous_peaks[idx] = current_peaks[idx]
    })
    current_peaks.forEach(function(v,idx){
      current_peaks[idx] = new_peaks[idx]
    })
    previous_peaks.forEach(function(previous_v,idx){
      // we are comparing the current peak value to the previous peak value
      var current_v = current_peaks[idx]

      // clear the new signals variable flag for this index
      new_signals[idx] = 0

      // search before and after?
      if(previous_v === 1 && current_v === 1){
        if(identified_signals[idx] === 0){
          // totally new signal found
          new_signals[idx] = 1
        }
        // running signal found for this index
        identified_signals[idx] = 1
      } else {
        // no running signal found for this index
        identified_signals[idx] = 0
      }
    })

    var found_signals = log_identified_signals()
    var found_signal_indexes = log_identified_signal_indexes()

    if(found_signals.length > 0){

      // var a = []
      // found_signals.forEach(function(v){
      //   a.push(Math.floor(v))
      // })
      // process.stdout.write(JSON.stringify(a))
      // process.stdout.write(' ')

      found_signal_indexes.forEach(function(i){
        running_identified_indexes[i] += 1
      })

      var all_found_signal_indexes = []
      running_identified_indexes.forEach(function(v,i){
        if(v>0){
          all_found_signal_indexes.push(i)
        }
      })

      // process.stdout.write(JSON.stringify(all_found_signal_indexes))

      var normalized_freqs = normalize_identified_signals(all_found_signal_indexes)

      var limit = 6
      normalized_freqs.forEach(function(f,i){
        if(i<limit){
          rpc.set('hunter_freq_'+i, f - frequency)
        }
      })

      // hunter_freq_0 = normalized_freqs[normalized_freqs.length-1] - frequency
      // rpc.set('hunter_freq_0', hunter_freq_0)
      // process.stdout.write(' setting frequency ' + hunter_freq_0)
      // process.stdout.write('\n')
    }

    current_identified_frequencies = found_signals
    current_identified_frequency_indexes = found_signal_indexes

  } // end of tick
  ////////////////////////////////////////////////////////////////////////////

  ////////////////////////
  function log_identified_signals(){
    var freqs = []
    identified_signals.forEach(function(v, idx){
      if(v === 1){
        freqs.push(scale_index_to_frequency(idx))
      }
    })
    return freqs
  }

  function log_identified_signal_indexes(){
    var indexes = []
    identified_signals.forEach(function(v, idx){
      if(v === 1){
        indexes.push(idx)
      }
    })
    return indexes
  }

  function normalize_identified_signals(idxes){
    // breaks the streaks of indexes into a flat list of single frequencies
    // containing the value of the median of the group
    var peak_distance_limit = 10
    var groups = []
    var current_group = []
    idxes.forEach(function(v,i){
      current_group.push(scale_index_to_frequency(v))
      if(i < idxes.length-1){
        var next_v = idxes[i+1]
        if(next_v-v > peak_distance_limit){
          // console.log('group break', v, next_v)
          groups.push(current_group)
          current_group = []
        }
      }
    })
    if(current_group.length > 0){
      groups.push(current_group)
    }
    // console.log(JSON.stringify(groups))
    var good_freqs = []
    groups.forEach(function(group){
      var v0 = group[0]
      var v1 = group[group.length-1]
      var s = (v0 + v1) * 0.5
      if(Math.abs(frequency-s) > 10000){
        good_freqs.push(Math.floor(s))
      }
    })
    console.log(good_freqs)
    return good_freqs
  }

  // function log_new_signals(){
  //   var freqs = []
  //   new_signals.forEach(function(v, idx){
  //     if(v === 1){
  //       freqs.push(scale_index_to_frequency(idx))
  //     }
  //   })
  //   return freqs
  // }

  function set_frequency(f){
    frequency = f
  }
  function get_frequency(f){
    return frequency
  }

  function iq_packet(buffer){
    recorder.add_buffer(buffer)
  }

  function rpc_update(cb){
    var fns = []
    fns.push(function(next){
      rpc.get('frequency', function(v){
        frequency = v
        next()
      })
    })
    fns.push(function(next){
      rpc.get('samp_rate', function(v){
        samp_rate = v
        next()
      })
    })
    fns.push(function(next){
      cb({
        frequency: frequency,
        samp_rate: samp_rate
      })
      next()
    })
    async.series(fns)
  }

  function peak_status(){
    return {
      freqs: current_identified_frequencies,
      indexes: current_identified_frequency_indexes
    }
  }

  return {
    tick: tick,
    set_frequency: set_frequency,
    get_frequency: get_frequency,
    iq_packet: iq_packet,
    rpc_update: rpc_update,
    peak_status: peak_status
  }
}
