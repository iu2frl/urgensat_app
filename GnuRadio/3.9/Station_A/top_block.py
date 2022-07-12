#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.9.7.0

from gnuradio import blocks
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import digital
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import grnet




class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.grnet_tcp_source_0 = grnet.tcp_source.tcp_source(
        	itemsize=gr.sizeof_char*1,
        	addr='127.0.0.1',
        	port=5001,
        	server=True,
        )
        self.grnet_tcp_sink_0 = grnet.tcp_sink(gr.sizeof_char, 1, '127.0.0.1', 1238,1)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
            samples_per_symbol=2,
            bt=0.35,
            verbose=False,
            log=False,
            do_unpack=True)
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
            samples_per_symbol=2,
            gain_mu=0.175,
            mu=0.5,
            omega_relative_limit=0.005,
            freq_error=0.0,
            verbose=False,log=False)
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=50,
            frequency_offset=0.0,
            epsilon=1.0,
            taps=[1.0 + 1.0j],
            noise_seed=0,
            block_tags=False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(500)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_gmsk_demod_0, 0))
        self.connect((self.digital_gmsk_demod_0, 0), (self.grnet_tcp_sink_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.grnet_tcp_source_0, 0), (self.blocks_throttle_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)




def main(top_block_cls=top_block, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
