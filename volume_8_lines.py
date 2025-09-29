# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: volime_8_lines
# GNU Radio version: 3.10.10.0

from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal







class volume_8_lines(gr.hier_block2):
    def __init__(self, band_1_1=2, band_1_2=2, band_1_3=2, band_1_4=2, band_1_5=2, band_1_6=2, band_1_7=2, band_1_8=2, semp_rate_0=32000):
        gr.hier_block2.__init__(
            self, "volime_8_lines",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.band_1_1 = band_1_1
        self.band_1_2 = band_1_2
        self.band_1_3 = band_1_3
        self.band_1_4 = band_1_4
        self.band_1_5 = band_1_5
        self.band_1_6 = band_1_6
        self.band_1_7 = band_1_7
        self.band_1_8 = band_1_8
        self.semp_rate_0 = semp_rate_0

        ##################################################
        # Blocks
        ##################################################

        self.blocks_add_xx_0_1 = blocks.add_vff(1)
        self.band_pass_filter_0_1_9_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1_8,
                semp_rate_0,
                11400,
                15000,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1_9 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1_7,
                semp_rate_0,
                7700,
                11400,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1_8 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1_6,
                semp_rate_0,
                4000,
                7700,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1_7 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1_5,
                semp_rate_0,
                2750,
                4000,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1_6 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1_4,
                semp_rate_0,
                1500,
                2750,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1_5 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1_3,
                semp_rate_0,
                250,
                1500,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1_4 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1_2,
                semp_rate_0,
                115,
                250,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_1_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1_1,
                semp_rate_0,
                20,
                115,
                1,
                window.WIN_HAMMING,
                6.76))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0_1_3, 0), (self.blocks_add_xx_0_1, 1))
        self.connect((self.band_pass_filter_0_1_4, 0), (self.blocks_add_xx_0_1, 2))
        self.connect((self.band_pass_filter_0_1_5, 0), (self.blocks_add_xx_0_1, 3))
        self.connect((self.band_pass_filter_0_1_6, 0), (self.blocks_add_xx_0_1, 4))
        self.connect((self.band_pass_filter_0_1_7, 0), (self.blocks_add_xx_0_1, 5))
        self.connect((self.band_pass_filter_0_1_8, 0), (self.blocks_add_xx_0_1, 6))
        self.connect((self.band_pass_filter_0_1_9, 0), (self.blocks_add_xx_0_1, 7))
        self.connect((self.band_pass_filter_0_1_9_0, 0), (self.blocks_add_xx_0_1, 0))
        self.connect((self.blocks_add_xx_0_1, 0), (self, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_3, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_4, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_5, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_6, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_7, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_8, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_9, 0))
        self.connect((self, 0), (self.band_pass_filter_0_1_9_0, 0))


    def get_band_1_1(self):
        return self.band_1_1

    def set_band_1_1(self, band_1_1):
        self.band_1_1 = band_1_1
        self.band_pass_filter_0_1_3.set_taps(firdes.band_pass(self.band_1_1, self.semp_rate_0, 20, 115, 1, window.WIN_HAMMING, 6.76))

    def get_band_1_2(self):
        return self.band_1_2

    def set_band_1_2(self, band_1_2):
        self.band_1_2 = band_1_2
        self.band_pass_filter_0_1_4.set_taps(firdes.band_pass(self.band_1_2, self.semp_rate_0, 115, 250, 1, window.WIN_HAMMING, 6.76))

    def get_band_1_3(self):
        return self.band_1_3

    def set_band_1_3(self, band_1_3):
        self.band_1_3 = band_1_3
        self.band_pass_filter_0_1_5.set_taps(firdes.band_pass(self.band_1_3, self.semp_rate_0, 250, 1500, 1, window.WIN_HAMMING, 6.76))

    def get_band_1_4(self):
        return self.band_1_4

    def set_band_1_4(self, band_1_4):
        self.band_1_4 = band_1_4
        self.band_pass_filter_0_1_6.set_taps(firdes.band_pass(self.band_1_4, self.semp_rate_0, 1500, 2750, 1, window.WIN_HAMMING, 6.76))

    def get_band_1_5(self):
        return self.band_1_5

    def set_band_1_5(self, band_1_5):
        self.band_1_5 = band_1_5
        self.band_pass_filter_0_1_7.set_taps(firdes.band_pass(self.band_1_5, self.semp_rate_0, 2750, 4000, 1, window.WIN_HAMMING, 6.76))

    def get_band_1_6(self):
        return self.band_1_6

    def set_band_1_6(self, band_1_6):
        self.band_1_6 = band_1_6
        self.band_pass_filter_0_1_8.set_taps(firdes.band_pass(self.band_1_6, self.semp_rate_0, 4000, 7700, 1, window.WIN_HAMMING, 6.76))

    def get_band_1_7(self):
        return self.band_1_7

    def set_band_1_7(self, band_1_7):
        self.band_1_7 = band_1_7
        self.band_pass_filter_0_1_9.set_taps(firdes.band_pass(self.band_1_7, self.semp_rate_0, 7700, 11400, 1, window.WIN_HAMMING, 6.76))

    def get_band_1_8(self):
        return self.band_1_8

    def set_band_1_8(self, band_1_8):
        self.band_1_8 = band_1_8
        self.band_pass_filter_0_1_9_0.set_taps(firdes.band_pass(self.band_1_8, self.semp_rate_0, 11400, 15000, 1, window.WIN_HAMMING, 6.76))

    def get_semp_rate_0(self):
        return self.semp_rate_0

    def set_semp_rate_0(self, semp_rate_0):
        self.semp_rate_0 = semp_rate_0
        self.band_pass_filter_0_1_3.set_taps(firdes.band_pass(self.band_1_1, self.semp_rate_0, 20, 115, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_4.set_taps(firdes.band_pass(self.band_1_2, self.semp_rate_0, 115, 250, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_5.set_taps(firdes.band_pass(self.band_1_3, self.semp_rate_0, 250, 1500, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_6.set_taps(firdes.band_pass(self.band_1_4, self.semp_rate_0, 1500, 2750, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_7.set_taps(firdes.band_pass(self.band_1_5, self.semp_rate_0, 2750, 4000, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_8.set_taps(firdes.band_pass(self.band_1_6, self.semp_rate_0, 4000, 7700, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_9.set_taps(firdes.band_pass(self.band_1_7, self.semp_rate_0, 7700, 11400, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1_9_0.set_taps(firdes.band_pass(self.band_1_8, self.semp_rate_0, 11400, 15000, 1, window.WIN_HAMMING, 6.76))

