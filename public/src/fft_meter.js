var d3 = window.d3

module.exports = function fft_meter () {
  console.log('creating fft meter')
  var body = d3.select('div#meter')

  var w = 1024
  var h = 256

  var svg = body.append('svg')
    .attr('width', '100%')
    .attr('viewBox', '0 0 1024 256')
    .attr('preserveAspectRatio', 'xMidYMid')
    .style('outline', '1px solid rgb(100,100,100)')

  var scale_y_power = d3.scale.linear().domain([-3, 3]).range([h * 0.95, h * 0.05])
  var scale_x_frequency = d3.scale.linear().domain([0, 1024]).range([0, w])

  var pts = []
  var lines = []

  function create_pts () {
    var n_pts = 1024

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
    pts.forEach(function (pt, i) {
      pt.y = scale_y_power(data[i])
    })
    lines.forEach(function (line, i) {
      line.attr('y1', pts[i].y).attr('y2', pts[i + 1].y)
    })
  }

  return {
    update: update
  }

}
