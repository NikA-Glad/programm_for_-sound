#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Eho_show
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from ehooo_ import ehooo_  # grc-generated hier_block
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



class eho_show(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Eho_show", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Eho_show")
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

        self.settings = Qt.QSettings("GNU Radio", "eho_show")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 0
        self.samp_rate = samp_rate = 32000
        self.delay__ = delay__ = 100

        ##################################################
        # Blocks
        ##################################################

        # Create the options list
        self._variable_qtgui_chooser_0_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_0_labels = ['Audio Source', 'Wav File']
        # Create the combo box
        self._variable_qtgui_chooser_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_0_tool_bar.addWidget(Qt.QLabel("Chooser_audio" + ": "))
        self._variable_qtgui_chooser_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_0_tool_bar.addWidget(self._variable_qtgui_chooser_0_combo_box)
        for _label in self._variable_qtgui_chooser_0_labels: self._variable_qtgui_chooser_0_combo_box.addItem(_label)
        self._variable_qtgui_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_options.index(i)))
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self._variable_qtgui_chooser_0_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_0(self._variable_qtgui_chooser_0_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_tool_bar)
        self._delay___range = qtgui.Range(100, 10000, 100, 100, 200)
        self._delay___win = qtgui.RangeWidget(self._delay___range, self.set_delay__, "Delay__", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay___win)
        self.ehooo_0 = ehooo_(
            delay__=delay__,
        )
        self.blocks_wavfile_source_1 = blocks.wavfile_source('C:\\123\\eho_voice.wav', False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            'C:\\123\\eho_voice__2.wav',
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_selector_0_0_0 = blocks.selector(gr.sizeof_float*1,variable_qtgui_chooser_0,0)
        self.blocks_selector_0_0_0.set_enabled(True)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, (32000*3))
        self.audio_source_0_1 = audio.source(samp_rate, '', True)
        self.audio_sink_0_1 = audio.sink(samp_rate, '', False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0_1, 0), (self.blocks_selector_0_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_selector_0_0_0, 0), (self.ehooo_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_selector_0_0_0, 1))
        self.connect((self.blocks_wavfile_source_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.ehooo_0, 0), (self.audio_sink_0_1, 0))
        self.connect((self.ehooo_0, 0), (self.blocks_wavfile_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "eho_show")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self.blocks_selector_0_0_0.set_input_index(self.variable_qtgui_chooser_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)

    def get_delay__(self):
        return self.delay__

    def set_delay__(self, delay__):
        self.delay__ = delay__
        self.ehooo_0.set_delay__(self.delay__)




def main(top_block_cls=eho_show, options=None):

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
