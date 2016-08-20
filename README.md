# signal hunter

Gnuradio application receives IQ stream from RTLSDR.  Gnuradio performs an FFT on the IQ stream and outputs the vector across ZMQ to node.  Node searches for peaks in the FFT vector.  When it finds a peak it records the time and the frequency.

The node application also collects the IQ stream from ZMQ and buffers multiple seconds.  When a peak is found the IQ stream is recorded to disk.

# todo

* [x] buffer stats
  * [x] max, min, average, median
  * [x] baseline level detection
  * [x] peak detection > list of frequencies

* [x] Signal Hunter
  * [x] set / get frequency
  * [x] draw buffer waterfall in the console
  * [x] signal detection from peaks

* [ ] IQ stream recorder
  * [x] test write iq stream
  * [ ] buffer iq stream
  * [x] move to signal hunter codebase
  * [x] have zmq event populate signal hunter object
  * [ ] compression

* [ ] Signal Event Recorder
  * [ ] emit blob to database

* [ ] record fft
  * [ ] data blob
  * [ ] metadata
    * [ ] frequency
    * [ ] time

* [ ] browser interoperability
  * [ ] get frequency
  * [ ] set frequency
  * [ ] turn step on / off
  * [ ] set step frequency size
  * [ ] set step time interval
  * [ ] max, min, average, median, baseline
  * [x] visualize FFT
  * [ ] identify peaks
  * [ ] recording state
