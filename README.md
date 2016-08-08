# signal hunter

Gnuradio application receives IQ stream from RTLSDR.  Gnuradio performs an FFT on the IQ stream and outputs the vector across ZMQ to node.  Node searches for peaks in the FFT vector.  When it finds a peak it records the time and the frequency.
