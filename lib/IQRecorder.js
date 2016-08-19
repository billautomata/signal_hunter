var Buffer = require('buffer').Buffer
var fs = require('fs')
var zlib = require('zlib')


module.exports = function IQRecorder(){

  var ring_buffer = Array(10)
  var ring_buffer_current_index = 0

  var is_recording = false
  var ticks_remaining = 0
  var recording_age = 0
  var max_age = 2

  var recording_buffers = []

  function add_buffer(buffer){
    // console.log('adding buffer at index', ring_buffer_current_index, ' recording_age ', recording_age)
    ring_buffer[ring_buffer_current_index] = buffer
    ring_buffer_current_index += 1
    if(ring_buffer_current_index >= ring_buffer.length){
      ring_buffer_current_index = 0
    }

    if(is_recording){
      recording_buffers.push(buffer)
      ticks_remaining -= 1
      recording_age += 1
      console.log('adding iq buffer to recording stack ', ticks_remaining, ' ticks remaining')
      if(ticks_remaining < 0){
        console.log('ending recording because no more ticks remaining')
        end_recording()
      }
      if(recording_age > max_age){
        console.log('ending recording because recording_age is too high')
        end_recording()
      }
    }
  }

  function start_recording(ticks, history_size){
    if(is_recording){
      console.log('is already recording')
      if(ticks_remaining < max_age){
        ticks_remaining += ticks
      }
      return
    }
    console.log('starting new recording')

    is_recording = true
    ticks_remaining = ticks
    recording_age = 0

    // add history_size to recording_buffers
    for(var i = 0; i < history_size; i++){
      var index_to_push = (ring_buffer_current_index - history_size + i)
      if(index_to_push < 0){
        index_to_push += ring_buffer.length
      }
      if(ring_buffer[index_to_push] !== undefined){
        recording_buffers.push(ring_buffer[index_to_push])
      }
    }

  }

  function end_recording(){
    // create uuid
    var filename = './iq_files/'+ Date.now() + '.iq.gz'
    is_recording = false
    ticks_remaining = 0
    recording_age = 0
    // zlib.deflate(Buffer.concat(recording_buffers), function(err, buffer){
    //   fs.writeFileSync(filename, buffer)
    // })
    recording_buffers = []
  }

  return {
    add_buffer: add_buffer,
    start_recording: start_recording
  }

}
