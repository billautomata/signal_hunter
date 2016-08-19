console.log(Date.now())
console.log('lol')

// var d3 = window.d3
// var svg = d3.select('div#main').append('svg')

var meter = require('./fft_meter.js')()

function render () {
  window.requestAnimationFrame(render)
}
render()

window.latest_buffer = []
window.socket.on('fft_data', function (d) {
  console.log(d.length)
  window.latest_buffer = d

  meter.update(d)

})

window.socket.on('frequency', function (d) {
  console.log('got frequency!')
  console.log(d)
})
