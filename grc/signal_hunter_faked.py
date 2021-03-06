#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Signal Hunter Faked
# Author: @billautomata
# Description: yes
# Generated: Mon Aug 22 10:17:37 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import SimpleXMLRPCServer
import threading
import wx


class signal_hunter_faked(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Signal Hunter Faked")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2000000
        self.xlate_decimation = xlate_decimation = 40
        self.offset2 = offset2 = 0
        self.offset = offset = samp_rate/4
        self.hunter_freq_0 = hunter_freq_0 = 0
        self.gain = gain = 10
        self.frequency = frequency = 930000000
        self.filter_width = filter_width = 5120
        self.fft_taps = fft_taps = filter.firdes.low_pass_2(1, samp_rate, 2000, 1000, 0.1)

        ##################################################
        # Blocks
        ##################################################
        _offset2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset2_sizer,
        	value=self.offset2,
        	callback=self.set_offset2,
        	label='offset2',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._offset2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset2_sizer,
        	value=self.offset2,
        	callback=self.set_offset2,
        	minimum=-samp_rate/2,
        	maximum=samp_rate/2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_offset2_sizer)
        _offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	label='offset',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	minimum=-samp_rate/2,
        	maximum=samp_rate/2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_offset_sizer)
        _hunter_freq_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hunter_freq_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_0_sizer,
        	value=self.hunter_freq_0,
        	callback=self.set_hunter_freq_0,
        	label='hunter_freq_0',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._hunter_freq_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_0_sizer,
        	value=self.hunter_freq_0,
        	callback=self.set_hunter_freq_0,
        	minimum=-100000,
        	maximum=100000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_hunter_freq_0_sizer)
        _frequency_sizer = wx.BoxSizer(wx.VERTICAL)
        self._frequency_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_frequency_sizer,
        	value=self.frequency,
        	callback=self.set_frequency,
        	label='Frequency',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._frequency_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_frequency_sizer,
        	value=self.frequency,
        	callback=self.set_frequency,
        	minimum=80000000,
        	maximum=1100000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_frequency_sizer)
        self.zeromq_push_sink_1 = zeromq.push_sink(gr.sizeof_gr_complex, samp_rate, 'tcp://127.0.0.1:9001', 100, False, -1)
        self.zeromq_push_sink_0_0 = zeromq.push_sink(gr.sizeof_float, 1024, 'tcp://127.0.0.1:9000', 100, False, -1)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost', 8080), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate/xlate_decimation,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='filtered_fft',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=frequency,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='master_plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        _gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	label='gain',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	minimum=0,
        	maximum=50,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_gain_sizer)
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(xlate_decimation, (fft_taps), frequency + hunter_freq_0, samp_rate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        _filter_width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._filter_width_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_filter_width_sizer,
        	value=self.filter_width,
        	callback=self.set_filter_width,
        	label='filter_width',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._filter_width_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_filter_width_sizer,
        	value=self.filter_width,
        	callback=self.set_filter_width,
        	minimum=2048,
        	maximum=40960,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_filter_width_sizer)
        self.fft_vxx_0 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 1024)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_2 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_float*1, 1024)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, frequency+offset, 0.001, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, frequency+offset2, 0.001, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_to_vector_2, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_stream_to_vector_1, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_stream_to_vector_1, 0), (self.zeromq_push_sink_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_2, 0), (self.zeromq_push_sink_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.wxgui_fftsink2_0_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_offset(self.samp_rate/4)
        self.set_fft_taps(filter.firdes.low_pass_2(1, self.samp_rate, 2000, 1000, 0.1))
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate/self.xlate_decimation)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_xlate_decimation(self):
        return self.xlate_decimation

    def set_xlate_decimation(self, xlate_decimation):
        self.xlate_decimation = xlate_decimation
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate/self.xlate_decimation)

    def get_offset2(self):
        return self.offset2

    def set_offset2(self, offset2):
        self.offset2 = offset2
        self._offset2_slider.set_value(self.offset2)
        self._offset2_text_box.set_value(self.offset2)
        self.analog_sig_source_x_0.set_frequency(self.frequency+self.offset2)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self._offset_slider.set_value(self.offset)
        self._offset_text_box.set_value(self.offset)
        self.analog_sig_source_x_0_0.set_frequency(self.frequency+self.offset)

    def get_hunter_freq_0(self):
        return self.hunter_freq_0

    def set_hunter_freq_0(self, hunter_freq_0):
        self.hunter_freq_0 = hunter_freq_0
        self._hunter_freq_0_slider.set_value(self.hunter_freq_0)
        self._hunter_freq_0_text_box.set_value(self.hunter_freq_0)
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.frequency + self.hunter_freq_0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self._frequency_slider.set_value(self.frequency)
        self._frequency_text_box.set_value(self.frequency)
        self.wxgui_fftsink2_0.set_baseband_freq(self.frequency)
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.frequency + self.hunter_freq_0)
        self.analog_sig_source_x_0_0.set_frequency(self.frequency+self.offset)
        self.analog_sig_source_x_0.set_frequency(self.frequency+self.offset2)

    def get_filter_width(self):
        return self.filter_width

    def set_filter_width(self, filter_width):
        self.filter_width = filter_width
        self._filter_width_slider.set_value(self.filter_width)
        self._filter_width_text_box.set_value(self.filter_width)

    def get_fft_taps(self):
        return self.fft_taps

    def set_fft_taps(self, fft_taps):
        self.fft_taps = fft_taps
        self.freq_xlating_fft_filter_ccc_0.set_taps((self.fft_taps))


def main(top_block_cls=signal_hunter_faked, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
