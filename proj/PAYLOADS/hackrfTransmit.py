#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Hackrftransmit
# Generated: Tue Aug 15 21:02:04 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class hackrfTransmit(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Hackrftransmit")

        ##################################################
        # Variables
        ##################################################
        self.audio_samp = audio_samp = 44100
        self.samp_rate = samp_rate = 1.03e6
        self.quad_rate = quad_rate = audio_samp*3
        self.freq = freq = 915e5

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=8,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(14, 0)
        self.osmosdr_sink_0.set_if_gain(47, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/root/proj/MUSIC/DangerZone.wav", True)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(samp_rate)/2)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=audio_samp,
        	quad_rate=quad_rate,
        	tau=75e-6,
        	max_dev=75e3,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.analog_wfm_tx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_delay_0, 0))    

    def get_audio_samp(self):
        return self.audio_samp

    def set_audio_samp(self, audio_samp):
        self.audio_samp = audio_samp
        self.set_quad_rate(self.audio_samp*3)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_delay_0.set_dly(int(self.samp_rate)/2)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_sink_0.set_center_freq(self.freq, 0)


def main(top_block_cls=hackrfTransmit, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
