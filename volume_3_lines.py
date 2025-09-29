# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: volume_3_lines
# GNU Radio version: 3.10.10.0

from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal







class volume_3_lines(gr.hier_block2):
    def __init__(self, band_0_0=2, band_0_1=2, band_0_2=2, samp_rate=32000):
        gr.hier_block2.__init__(
            self, "volume_3_lines",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.band_0_0 = band_0_0
        self.band_0_1 = band_0_1
        self.band_0_2 = band_0_2
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_1_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_0_1,
                samp_rate,
                250,
                4000,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_0_0,
                samp_rate,
                4000,
                15000,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_0_2,
                samp_rate,
                20,
                250,
                1,
                window.WIN_HAMMING,
                6.76))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_1_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_0_1_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_0, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_1, 0))


    def get_band_0_0(self):
        return self.band_0_0

    def set_band_0_0(self, band_0_0):
        self.band_0_0 = band_0_0
        self.band_pass_filter_0_1_0.set_taps(firdes.band_pass(self.band_0_0, self.samp_rate, 4000, 15000, 1, window.WIN_HAMMING, 6.76))

    def get_band_0_1(self):
        return self.band_0_1

    def set_band_0_1(self, band_0_1):
        self.band_0_1 = band_0_1
        self.band_pass_filter_0_1_1.set_taps(firdes.band_pass(self.band_0_1, self.samp_rate, 250, 4000, 1, window.WIN_HAMMING, 6.76))

    def get_band_0_2(self):
        return self.band_0_2

    def set_band_0_2(self, band_0_2):
        self.band_0_2 = band_0_2
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.band_0_2, self.samp_rate, 20, 250, 1, window.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.band_0_2, self.samp_rate, 20, 250, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_0.set_taps(firdes.band_pass(self.band_0_0, self.samp_rate, 4000, 15000, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_1.set_taps(firdes.band_pass(self.band_0_1, self.samp_rate, 250, 4000, 1, window.WIN_HAMMING, 6.76))

