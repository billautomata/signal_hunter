console.log(Date.now())
console.log('lol')

// var d3 = window.d3
// var svg = d3.select('div#main').append('svg')
window.latest_buffer = []
window.current_peak_data = {
  freqs: [],
  indexes: []
}

var meter = require('./fft_meter.js')()

function render () {
  meter.update(window.latest_buffer)
  window.requestAnimationFrame(render)
}
render()

window.socket.on('fft_data', function (d) {
  console.log(d.length)
  window.latest_buffer = d
})

window.socket.on('radio_data', function (d) {
  console.log('got radio data')
  console.log(d)
})

window.socket.on('peak_data', function (d) {
  console.log('got peak data')
  console.log(d)
  window.current_peak_data = d
})

window.socket.emit('get_frequency')
