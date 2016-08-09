console.log(Date.now())
console.log('lol')

// var d3 = window.d3
// var svg = d3.select('div#main').append('svg')

var veclen = 8192

for (var i = 0; i < veclen; i++) {
  // svg.append('circle').attr('cx',0)
}

function render () {
  window.requestAnimationFrame(render)
}
render()

window.latest_buffer = []
window.socket.on('fft_data', function (d) {
  console.log(d.length)
  window.latest_buffer = d
})
