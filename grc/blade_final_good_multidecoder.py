#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Pager 6Ch Decode
# Author: @billautomata
# Description: yes
# Generated: Wed Aug 24 08:04:23 2016
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

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio import zeromq
from gnuradio import pager
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import SimpleXMLRPCServer
import osmosdr
import threading
import time
import wx


class pager_6ch_decode(grc_wxgui.top_block_gui):

    def __init__(self, queue):
        grc_wxgui.top_block_gui.__init__(self, title="Pager 6Ch Decode")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 4000000
        self.xlate_decimation = xlate_decimation = 160
        self.hunter_freq_5 = hunter_freq_5 = 0
        self.hunter_freq_4 = hunter_freq_4 = 0
        self.hunter_freq_3 = hunter_freq_3 = 0
        self.hunter_freq_2 = hunter_freq_2 = 0
        self.hunter_freq_1 = hunter_freq_1 = 0
        self.hunter_freq_0 = hunter_freq_0 = 0
        self.gain = gain = 10
        self.frequency = frequency = 929000000
        self.filter_width = filter_width = 5120
        self.fft_taps = fft_taps = filter.firdes.low_pass_2(1, samp_rate, 2000, 1000, 0.1)
        self.fft_n_elements = fft_n_elements = 2048

        ##################################################
        # Blocks
        ##################################################
        _hunter_freq_5_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hunter_freq_5_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_5_sizer,
        	value=self.hunter_freq_5,
        	callback=self.set_hunter_freq_5,
        	label='hunter_freq_5',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._hunter_freq_5_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_5_sizer,
        	value=self.hunter_freq_5,
        	callback=self.set_hunter_freq_5,
        	minimum=-5000000,
        	maximum=5000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_hunter_freq_5_sizer)
        _hunter_freq_4_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hunter_freq_4_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_4_sizer,
        	value=self.hunter_freq_4,
        	callback=self.set_hunter_freq_4,
        	label='hunter_freq_4',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._hunter_freq_4_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_4_sizer,
        	value=self.hunter_freq_4,
        	callback=self.set_hunter_freq_4,
        	minimum=-5000000,
        	maximum=5000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_hunter_freq_4_sizer)
        _hunter_freq_3_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hunter_freq_3_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_3_sizer,
        	value=self.hunter_freq_3,
        	callback=self.set_hunter_freq_3,
        	label='hunter_freq_3',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._hunter_freq_3_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_3_sizer,
        	value=self.hunter_freq_3,
        	callback=self.set_hunter_freq_3,
        	minimum=-5000000,
        	maximum=5000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_hunter_freq_3_sizer)
        _hunter_freq_2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hunter_freq_2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_2_sizer,
        	value=self.hunter_freq_2,
        	callback=self.set_hunter_freq_2,
        	label='hunter_freq_2',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._hunter_freq_2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_2_sizer,
        	value=self.hunter_freq_2,
        	callback=self.set_hunter_freq_2,
        	minimum=-5000000,
        	maximum=5000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_hunter_freq_2_sizer)
        _hunter_freq_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hunter_freq_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_1_sizer,
        	value=self.hunter_freq_1,
        	callback=self.set_hunter_freq_1,
        	label='hunter_freq_1',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._hunter_freq_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hunter_freq_1_sizer,
        	value=self.hunter_freq_1,
        	callback=self.set_hunter_freq_1,
        	minimum=-5000000,
        	maximum=5000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_hunter_freq_1_sizer)
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
        	minimum=-5000000,
        	maximum=5000000,
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
        self.zeromq_push_sink_0_0 = zeromq.push_sink(gr.sizeof_float, fft_n_elements, 'tcp://127.0.0.1:9000', 100, False, -1)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost', 8080), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
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
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(frequency, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(40, 0)
        self.rtlsdr_source_0.set_if_gain(0, 0)
        self.rtlsdr_source_0.set_bb_gain(0, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(samp_rate, 0)

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
        self.freq_xlating_fft_filter_ccc_0_0_3 = filter.freq_xlating_fft_filter_ccc(xlate_decimation, (fft_taps), frequency + hunter_freq_5, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0_3.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0_3.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0_0_2 = filter.freq_xlating_fft_filter_ccc(xlate_decimation, (fft_taps), frequency + hunter_freq_4, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0_2.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0_2.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0_0_1 = filter.freq_xlating_fft_filter_ccc(xlate_decimation, (fft_taps), frequency + hunter_freq_3, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0_1.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0_1.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0_0_0 = filter.freq_xlating_fft_filter_ccc(xlate_decimation, (fft_taps), frequency + hunter_freq_2, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0_0.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0_0 = filter.freq_xlating_fft_filter_ccc(xlate_decimation, (fft_taps), frequency + hunter_freq_1, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0.declare_sample_delay(0)
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
        self.fft_vxx_0 = fft.fft_vcc(fft_n_elements, True, (window.blackmanharris(fft_n_elements)), True, 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_n_elements)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_float*1, fft_n_elements)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_n_elements)
        self.blocks_null_sink_0_0_3 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_2 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)

        # FLEX protocol demodulator
        self.flex0 = pager.flex_demod(queue, 0, False, False) # options.verbose, options.log
        self.flex1 = pager.flex_demod(queue, 0, False, False) # options.verbose, options.log
        self.flex2 = pager.flex_demod(queue, 0, False, False) # options.verbose, options.log
        self.flex3 = pager.flex_demod(queue, 0, False, False) # options.verbose, options.log
        self.flex4 = pager.flex_demod(queue, 0, False, False) # options.verbose, options.log
        self.flex5 = pager.flex_demod(queue, 0, False, False) # options.verbose, options.log

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.zeromq_push_sink_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.flex0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.flex1, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0_0_0, 0), (self.flex2, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0_0_1, 0), (self.flex3, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0_0_2, 0), (self.flex4, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0_0_3, 0), (self.flex5, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0_1, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0_2, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0_3, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_fftsink2_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_fft_taps(filter.firdes.low_pass_2(1, self.samp_rate, 2000, 1000, 0.1))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_xlate_decimation(self):
        return self.xlate_decimation

    def set_xlate_decimation(self, xlate_decimation):
        self.xlate_decimation = xlate_decimation

    def get_hunter_freq_5(self):
        return self.hunter_freq_5

    def set_hunter_freq_5(self, hunter_freq_5):
        self.hunter_freq_5 = hunter_freq_5
        self._hunter_freq_5_slider.set_value(self.hunter_freq_5)
        self._hunter_freq_5_text_box.set_value(self.hunter_freq_5)
        self.freq_xlating_fft_filter_ccc_0_0_3.set_center_freq(self.frequency + self.hunter_freq_5)

    def get_hunter_freq_4(self):
        return self.hunter_freq_4

    def set_hunter_freq_4(self, hunter_freq_4):
        self.hunter_freq_4 = hunter_freq_4
        self._hunter_freq_4_slider.set_value(self.hunter_freq_4)
        self._hunter_freq_4_text_box.set_value(self.hunter_freq_4)
        self.freq_xlating_fft_filter_ccc_0_0_2.set_center_freq(self.frequency + self.hunter_freq_4)

    def get_hunter_freq_3(self):
        return self.hunter_freq_3

    def set_hunter_freq_3(self, hunter_freq_3):
        self.hunter_freq_3 = hunter_freq_3
        self._hunter_freq_3_slider.set_value(self.hunter_freq_3)
        self._hunter_freq_3_text_box.set_value(self.hunter_freq_3)
        self.freq_xlating_fft_filter_ccc_0_0_1.set_center_freq(self.frequency + self.hunter_freq_3)

    def get_hunter_freq_2(self):
        return self.hunter_freq_2

    def set_hunter_freq_2(self, hunter_freq_2):
        self.hunter_freq_2 = hunter_freq_2
        self._hunter_freq_2_slider.set_value(self.hunter_freq_2)
        self._hunter_freq_2_text_box.set_value(self.hunter_freq_2)
        self.freq_xlating_fft_filter_ccc_0_0_0.set_center_freq(self.frequency + self.hunter_freq_2)

    def get_hunter_freq_1(self):
        return self.hunter_freq_1

    def set_hunter_freq_1(self, hunter_freq_1):
        self.hunter_freq_1 = hunter_freq_1
        self._hunter_freq_1_slider.set_value(self.hunter_freq_1)
        self._hunter_freq_1_text_box.set_value(self.hunter_freq_1)
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq(self.frequency + self.hunter_freq_1)

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
        self.rtlsdr_source_0.set_center_freq(self.frequency, 0)
        self.freq_xlating_fft_filter_ccc_0_0_3.set_center_freq(self.frequency + self.hunter_freq_5)
        self.freq_xlating_fft_filter_ccc_0_0_2.set_center_freq(self.frequency + self.hunter_freq_4)
        self.freq_xlating_fft_filter_ccc_0_0_1.set_center_freq(self.frequency + self.hunter_freq_3)
        self.freq_xlating_fft_filter_ccc_0_0_0.set_center_freq(self.frequency + self.hunter_freq_2)
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq(self.frequency + self.hunter_freq_1)
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.frequency + self.hunter_freq_0)

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
        self.freq_xlating_fft_filter_ccc_0_0_3.set_taps((self.fft_taps))
        self.freq_xlating_fft_filter_ccc_0_0_2.set_taps((self.fft_taps))
        self.freq_xlating_fft_filter_ccc_0_0_1.set_taps((self.fft_taps))
        self.freq_xlating_fft_filter_ccc_0_0_0.set_taps((self.fft_taps))
        self.freq_xlating_fft_filter_ccc_0_0.set_taps((self.fft_taps))
        self.freq_xlating_fft_filter_ccc_0.set_taps((self.fft_taps))

    def get_fft_n_elements(self):
        return self.fft_n_elements

    def set_fft_n_elements(self, fft_n_elements):
        self.fft_n_elements = fft_n_elements


def main(top_block_cls=pager_6ch_decode, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    queue = gr.msg_queue()
    tb = top_block_cls(queue)
    runner = pager.queue_runner(queue)
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
