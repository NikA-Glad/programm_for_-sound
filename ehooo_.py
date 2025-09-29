# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ehooo_00
# GNU Radio version: 3.10.10.0

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from delay_0 import delay_0  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal







class ehooo_(gr.hier_block2):
    def __init__(self, delay__=0):
        gr.hier_block2.__init__(
            self, "ehooo_00",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.delay__ = delay__

        ##################################################
        # Blocks
        ##################################################

        self.delay_0_0_0_0_1 = delay_0(
            delay=delay__,
            variable_qtgui_range_1=8,
        )
        self.delay_0_0_0_0_0 = delay_0(
            delay=(2*delay__),
            variable_qtgui_range_1=5,
        )
        self.delay_0_0_0_0 = delay_0(
            delay=(delay__*3),
            variable_qtgui_range_1=2,
        )
        self.delay_0_0_0 = delay_0(
            delay=(delay__*4),
            variable_qtgui_range_1=0.5,
        )
        self.delay_0_0 = delay_0(
            delay=(delay__*5),
            variable_qtgui_range_1=0,
        )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(10)
        self.blocks_add_xx_0 = blocks.add_vff(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.delay_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.delay_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.delay_0_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.delay_0_0_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.delay_0_0_0_0_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self, 0), (self.delay_0_0, 0))
        self.connect((self, 0), (self.delay_0_0_0, 0))
        self.connect((self, 0), (self.delay_0_0_0_0, 0))
        self.connect((self, 0), (self.delay_0_0_0_0_0, 0))
        self.connect((self, 0), (self.delay_0_0_0_0_1, 0))


    def get_delay__(self):
        return self.delay__

    def set_delay__(self, delay__):
        self.delay__ = delay__
        self.delay_0_0.set_delay((self.delay__*5))
        self.delay_0_0_0.set_delay((self.delay__*4))
        self.delay_0_0_0_0.set_delay((self.delay__*3))
        self.delay_0_0_0_0_0.set_delay((2*self.delay__))
        self.delay_0_0_0_0_1.set_delay(self.delay__)

