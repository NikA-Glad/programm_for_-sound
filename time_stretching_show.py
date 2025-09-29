#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Time_Stretching_show
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx



class time_stretching_show(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Time_Stretching_show", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Time_Stretching_show")
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

        self.settings = Qt.QSettings("GNU Radio", "time_stretching_show")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.speed_0 = speed_0 = 20000
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        self._speed_0_tool_bar = Qt.QToolBar(self)
        self._speed_0_tool_bar.addWidget(Qt.QLabel("Speed" + ": "))
        self._speed_0_line_edit = Qt.QLineEdit(str(self.speed_0))
        self._speed_0_tool_bar.addWidget(self._speed_0_line_edit)
        self._speed_0_line_edit.returnPressed.connect(
            lambda: self.set_speed_0(eng_notation.str_to_num(str(self._speed_0_line_edit.text()))))
        self.top_layout.addWidget(self._speed_0_tool_bar)
        self.blocks_wavfile_source_1 = blocks.wavfile_source('C:\\123\\eho_voice.wav', False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            'C:\\123\\nanana,.wav',
            1,
            (samp_rate+speed_0),
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_wavfile_source_1, 0), (self.blocks_wavfile_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "time_stretching_show")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_speed_0(self):
        return self.speed_0

    def set_speed_0(self, speed_0):
        self.speed_0 = speed_0
        Qt.QMetaObject.invokeMethod(self._speed_0_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.speed_0)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=time_stretching_show, options=None):

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
