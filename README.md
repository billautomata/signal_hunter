# signal hunter

Gnuradio application receives IQ stream from RTLSDR.  Gnuradio performs an FFT on the IQ stream and outputs the vector across ZMQ to node.  Node searches for peaks in the FFT vector.  When it finds a peak it records the time and the frequency.

The node application also collects the IQ stream from ZMQ and buffers multiple seconds.  When a peak is found the IQ stream is recorded to disk.


# todo

* [x] buffer stats
  * [x] max, min, average, median
  * [ ] baseline level detection
  * [ ]
* [x] draw buffer waterfall in the console
* [ ] record iq stream
* [ ] set / get frequency
* [ ] record fft
  * [ ] data blob
  * [ ] metadata
    * [ ] frequency
    * [ ] time
* [ ] browser interoperability
  * [x] get frequency
  * [ ] set frequency
  * [ ] buffer stats
  * [ ] max, min, average, median
  * [ ] baseline level detection
