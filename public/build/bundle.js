(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
var d3 = window.d3

module.exports = function fft_meter () {
  console.log('creating fft meter')
  var body = d3.select('div#meter')

  var w = 2048
  var h = 512

  var svg = body.append('svg')
    .attr('width', '100%')
    .attr('viewBox', '0 0 ' + w + ' ' + h)
    .attr('preserveAspectRatio', 'xMidYMid')
    .style('outline', '1px solid rgb(100,100,100)')

  var auto_scale_input = [-3, 3]

  var scale_y_power = d3.scale.linear().domain(auto_scale_input).range([h * 0.95, h * 0.05])
  var scale_x_frequency = d3.scale.linear().domain([0, 2048]).range([0, w])

  var pts = []
  var lines = []

  function create_pts () {
    var n_pts = 2048

    for (var i = 0; i < n_pts; i++) {
      pts.push({
        x: scale_x_frequency(i),
        y: scale_y_power(0)
      })
    }
    for (var i = 0; i < n_pts - 1; i++) {
      lines.push(svg.append('line')
        .attr('x1', pts[i].x)
        .attr('y1', pts[i].y)
        .attr('x2', pts[i + 1].x)
        .attr('y2', pts[i + 1].y)
        .attr('stroke', 'black')
        .attr('fill', 'none')
      )
    }
  }

  create_pts()

  function update (data) {
    data.forEach(function (d, i) {
      if (d < auto_scale_input[0]) {
        auto_scale_input[0] = d
        scale_y_power = d3.scale.linear().domain(auto_scale_input).range([h * 0.95, h * 0.05])
      }
      if (d > auto_scale_input[1]) {
        auto_scale_input[1] = d
        scale_y_power = d3.scale.linear().domain(auto_scale_input).range([h * 0.95, h * 0.05])
      }
      auto_scale_input.forEach(function (d) {
        d *= 0.999
      })
      pts[i].y = scale_y_power(d)
    })
    lines.forEach(function (line, i) {
      line.attr('y1', pts[i].y).attr('y2', pts[i + 1].y).attr('stroke', 'black')
    })
    window.current_peak_data.indexes.forEach(function (idx) {
      lines[idx].attr('stroke', 'red')
    })
  }

  return {
    update: update
  }

}

},{}],2:[function(require,module,exports){
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
  // console.log(d.length)
  window.latest_buffer = d
})

window.socket.on('radio_data', function (d) {
  // console.log('got radio data')
  // console.log(d)
})

window.socket.on('peak_data', function (d) {
  // console.log('got peak data')
  // console.log(d)
  window.current_peak_data = d
})

window.socket.emit('get_frequency')

},{"./fft_meter.js":1}]},{},[2]);
