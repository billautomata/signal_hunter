(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
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

window.socket.on('frequency', function (d) {
  console.log('got frequency!')
  console.log(d)
})

},{}]},{},[1]);
