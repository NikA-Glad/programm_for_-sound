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
from reverb___01 import reverb___01  # grc-generated hier_block



class Rever_(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "Rever_")

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
        self.const = const = 0.01

        ##################################################
        # Blocks
        ##################################################

        self._delay_000_range = qtgui.Range(0, 1000, 10, 0, 200)
        self._delay_000_win = qtgui.RangeWidget(self._delay_000_range, self.set_delay_000, "Delay_000", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_000_win)
        self.reverb___01_0_1 = reverb___01(
            delay_000=(1000*3),
            variable_qtgui_range_1=0.1,
        )
        self.reverb___01_0_0 = reverb___01(
            delay_000=(1000*2),
            variable_qtgui_range_1=0.1,
        )
        self.reverb___01_0 = reverb___01(
            delay_000=1000,
            variable_qtgui_range_1=0.1,
        )
        self._const_range = qtgui.Range(0.01, 1, 0.05, 0.01, 200)
        self._const_win = qtgui.RangeWidget(self._const_range, self.set_const, "Costansta", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._const_win)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            'C:\\123\\zima,,.wav',
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(0.1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(10)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_source_0_1 = audio.source(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.reverb___01_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.reverb___01_0_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.reverb___01_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.reverb___01_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.reverb___01_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.reverb___01_0_1, 0), (self.blocks_add_xx_0, 2))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Rever_")
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

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const




def main(top_block_cls=Rever_, options=None):

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
