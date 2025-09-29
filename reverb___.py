#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import QtCore
from delay_0 import delay_0  # grc-generated hier_block
from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



class reverb___(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "reverb___")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.delay_000 = delay_000 = 0

        ##################################################
        # Blocks
        ##################################################

        self._delay_000_range = qtgui.Range(0, 1000, 10, 0, 200)
        self._delay_000_win = qtgui.RangeWidget(self._delay_000_range, self.set_delay_000, "Delay_000", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_000_win)
        self.delay_0_0_4 = delay_0(
            delay=(9*delay_000),
            variable_qtgui_range_1=4,
        )
        self.delay_0_0_3_0 = delay_0(
            delay=(13*delay_000),
            variable_qtgui_range_1=2,
        )
        self.delay_0_0_3 = delay_0(
            delay=(5*delay_000),
            variable_qtgui_range_1=6,
        )
        self.delay_0_0_2_1 = delay_0(
            delay=(12*delay_000),
            variable_qtgui_range_1=2.5,
        )
        self.delay_0_0_2_0_0 = delay_0(
            delay=(16*delay_000),
            variable_qtgui_range_1=0.5,
        )
        self.delay_0_0_2_0 = delay_0(
            delay=(8*delay_000),
            variable_qtgui_range_1=4.5,
        )
        self.delay_0_0_2 = delay_0(
            delay=(4*delay_000),
            variable_qtgui_range_1=6.5,
        )
        self.delay_0_0_1_1 = delay_0(
            delay=(11*delay_000),
            variable_qtgui_range_1=3,
        )
        self.delay_0_0_1_0_0 = delay_0(
            delay=(15*delay_000),
            variable_qtgui_range_1=1,
        )
        self.delay_0_0_1_0 = delay_0(
            delay=(7*delay_000),
            variable_qtgui_range_1=5,
        )
        self.delay_0_0_1 = delay_0(
            delay=(3*delay_000),
            variable_qtgui_range_1=7,
        )
        self.delay_0_0_0_1 = delay_0(
            delay=(10*delay_000),
            variable_qtgui_range_1=3.5,
        )
        self.delay_0_0_0_0_0 = delay_0(
            delay=(14*delay_000),
            variable_qtgui_range_1=1.5,
        )
        self.delay_0_0_0_0 = delay_0(
            delay=(6*delay_000),
            variable_qtgui_range_1=5.5,
        )
        self.delay_0_0_0 = delay_0(
            delay=(2*delay_000),
            variable_qtgui_range_1=7.5,
        )
        self.delay_0_0 = delay_0(
            delay=delay_000,
            variable_qtgui_range_1=8,
        )
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(0.1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(8)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_source_0_1 = audio.source(samp_rate, '', True)
        self.audio_sink_0_1 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_0_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_0_0_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_0_1, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_1, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_1_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_1_0_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_1_1, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_2, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_2_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_2_0_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_2_1, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_3, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_3_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.delay_0_0_4, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 16))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0_1, 0))
        self.connect((self.delay_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.delay_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.delay_0_0_0_0, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.delay_0_0_0_0_0, 0), (self.blocks_add_xx_0, 13))
        self.connect((self.delay_0_0_0_1, 0), (self.blocks_add_xx_0, 9))
        self.connect((self.delay_0_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.delay_0_0_1_0, 0), (self.blocks_add_xx_0, 6))
        self.connect((self.delay_0_0_1_0_0, 0), (self.blocks_add_xx_0, 14))
        self.connect((self.delay_0_0_1_1, 0), (self.blocks_add_xx_0, 10))
        self.connect((self.delay_0_0_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.delay_0_0_2_0, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.delay_0_0_2_0_0, 0), (self.blocks_add_xx_0, 15))
        self.connect((self.delay_0_0_2_1, 0), (self.blocks_add_xx_0, 11))
        self.connect((self.delay_0_0_3, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.delay_0_0_3_0, 0), (self.blocks_add_xx_0, 12))
        self.connect((self.delay_0_0_4, 0), (self.blocks_add_xx_0, 8))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "reverb___")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_delay_000(self):
        return self.delay_000

    def set_delay_000(self, delay_000):
        self.delay_000 = delay_000
        self.delay_0_0.set_delay(self.delay_000)
        self.delay_0_0_0.set_delay((2*self.delay_000))
        self.delay_0_0_0_0.set_delay((6*self.delay_000))
        self.delay_0_0_0_0_0.set_delay((14*self.delay_000))
        self.delay_0_0_0_1.set_delay((10*self.delay_000))
        self.delay_0_0_1.set_delay((3*self.delay_000))
        self.delay_0_0_1_0.set_delay((7*self.delay_000))
        self.delay_0_0_1_0_0.set_delay((15*self.delay_000))
        self.delay_0_0_1_1.set_delay((11*self.delay_000))
        self.delay_0_0_2.set_delay((4*self.delay_000))
        self.delay_0_0_2_0.set_delay((8*self.delay_000))
        self.delay_0_0_2_0_0.set_delay((16*self.delay_000))
        self.delay_0_0_2_1.set_delay((12*self.delay_000))
        self.delay_0_0_3.set_delay((5*self.delay_000))
        self.delay_0_0_3_0.set_delay((13*self.delay_000))
        self.delay_0_0_4.set_delay((9*self.delay_000))




def main(top_block_cls=reverb___, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
