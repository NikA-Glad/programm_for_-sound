# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: delay_
# GNU Radio version: 3.10.10.0

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class delay_0(gr.hier_block2):
    def __init__(self, delay=0, variable_qtgui_range_1=0):
        gr.hier_block2.__init__(
            self, "delay_",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.delay = delay
        self.variable_qtgui_range_1 = variable_qtgui_range_1

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_ff(variable_qtgui_range_1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, delay)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_delay_0, 0))


    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0.set_dly(int(self.delay))

    def get_variable_qtgui_range_1(self):
        return self.variable_qtgui_range_1

    def set_variable_qtgui_range_1(self, variable_qtgui_range_1):
        self.variable_qtgui_range_1 = variable_qtgui_range_1
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.variable_qtgui_range_1)

