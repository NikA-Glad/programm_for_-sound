#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Filter_show
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5.QtCore import QObject, pyqtSlot
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
from volume_3_lines import volume_3_lines  # grc-generated hier_block
import sip



class filter_show(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Filter_show", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Filter_show")
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

        self.settings = Qt.QSettings("GNU Radio", "filter_show")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_chooser_3 = variable_qtgui_chooser_3 = 0
        self.variable_qtgui_chooser_2 = variable_qtgui_chooser_2 = 0
        self.variable_qtgui_chooser_1 = variable_qtgui_chooser_1 = 0
        self.variable_qtgui_chooser = variable_qtgui_chooser = 0
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        # Create the options list
        self._variable_qtgui_chooser_3_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_3_labels = ['0', '1']
        # Create the combo box
        self._variable_qtgui_chooser_3_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_3_tool_bar.addWidget(Qt.QLabel("Chooser_audio" + ": "))
        self._variable_qtgui_chooser_3_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_3_tool_bar.addWidget(self._variable_qtgui_chooser_3_combo_box)
        for _label in self._variable_qtgui_chooser_3_labels: self._variable_qtgui_chooser_3_combo_box.addItem(_label)
        self._variable_qtgui_chooser_3_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_3_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_3_options.index(i)))
        self._variable_qtgui_chooser_3_callback(self.variable_qtgui_chooser_3)
        self._variable_qtgui_chooser_3_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_3(self._variable_qtgui_chooser_3_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_3_tool_bar)
        # Create the options list
        self._variable_qtgui_chooser_2_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_2_labels = ['0', '1']
        # Create the combo box
        self._variable_qtgui_chooser_2_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_2_tool_bar.addWidget(Qt.QLabel("Chooser_audio" + ": "))
        self._variable_qtgui_chooser_2_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_2_tool_bar.addWidget(self._variable_qtgui_chooser_2_combo_box)
        for _label in self._variable_qtgui_chooser_2_labels: self._variable_qtgui_chooser_2_combo_box.addItem(_label)
        self._variable_qtgui_chooser_2_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_2_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_2_options.index(i)))
        self._variable_qtgui_chooser_2_callback(self.variable_qtgui_chooser_2)
        self._variable_qtgui_chooser_2_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_2(self._variable_qtgui_chooser_2_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_2_tool_bar)
        # Create the options list
        self._variable_qtgui_chooser_1_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_1_labels = ['0', '1']
        # Create the combo box
        self._variable_qtgui_chooser_1_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_1_tool_bar.addWidget(Qt.QLabel("Chooser_audio" + ": "))
        self._variable_qtgui_chooser_1_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_1_tool_bar.addWidget(self._variable_qtgui_chooser_1_combo_box)
        for _label in self._variable_qtgui_chooser_1_labels: self._variable_qtgui_chooser_1_combo_box.addItem(_label)
        self._variable_qtgui_chooser_1_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_1_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_1_options.index(i)))
        self._variable_qtgui_chooser_1_callback(self.variable_qtgui_chooser_1)
        self._variable_qtgui_chooser_1_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_1(self._variable_qtgui_chooser_1_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_1_tool_bar)
        # Create the options list
        self._variable_qtgui_chooser_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_labels = ['Audio Source', 'Wav File']
        # Create the combo box
        self._variable_qtgui_chooser_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_tool_bar.addWidget(Qt.QLabel("Chooser_audio" + ": "))
        self._variable_qtgui_chooser_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_tool_bar.addWidget(self._variable_qtgui_chooser_combo_box)
        for _label in self._variable_qtgui_chooser_labels: self._variable_qtgui_chooser_combo_box.addItem(_label)
        self._variable_qtgui_chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_options.index(i)))
        self._variable_qtgui_chooser_callback(self.variable_qtgui_chooser)
        self._variable_qtgui_chooser_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser(self._variable_qtgui_chooser_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_tool_bar)
        self.volume_3_lines_0 = volume_3_lines(
            band_0_0=variable_qtgui_chooser_1,
            band_0_1=variable_qtgui_chooser_2,
            band_0_2=variable_qtgui_chooser_3,
            samp_rate=32000,
        )
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not False)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.blocks_wavfile_source_1 = blocks.wavfile_source('C:\\123\\nana.wav', False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            'C:\\123\\nana__2.wav',
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_selector_0_0_0 = blocks.selector(gr.sizeof_float*1,variable_qtgui_chooser,0)
        self.blocks_selector_0_0_0.set_enabled(True)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, (32000*3))
        self.audio_source_0_1 = audio.source(samp_rate, '', True)
        self.audio_sink_0_1 = audio.sink(samp_rate, '', False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0_1, 0), (self.blocks_selector_0_0_0, 0))
        self.connect((self.audio_source_0_1, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_selector_0_0_0, 0), (self.volume_3_lines_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_selector_0_0_0, 1))
        self.connect((self.blocks_wavfile_source_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.volume_3_lines_0, 0), (self.audio_sink_0_1, 0))
        self.connect((self.volume_3_lines_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.volume_3_lines_0, 0), (self.qtgui_freq_sink_x_0_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "filter_show")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_chooser_3(self):
        return self.variable_qtgui_chooser_3

    def set_variable_qtgui_chooser_3(self, variable_qtgui_chooser_3):
        self.variable_qtgui_chooser_3 = variable_qtgui_chooser_3
        self._variable_qtgui_chooser_3_callback(self.variable_qtgui_chooser_3)
        self.volume_3_lines_0.set_band_0_2(self.variable_qtgui_chooser_3)

    def get_variable_qtgui_chooser_2(self):
        return self.variable_qtgui_chooser_2

    def set_variable_qtgui_chooser_2(self, variable_qtgui_chooser_2):
        self.variable_qtgui_chooser_2 = variable_qtgui_chooser_2
        self._variable_qtgui_chooser_2_callback(self.variable_qtgui_chooser_2)
        self.volume_3_lines_0.set_band_0_1(self.variable_qtgui_chooser_2)

    def get_variable_qtgui_chooser_1(self):
        return self.variable_qtgui_chooser_1

    def set_variable_qtgui_chooser_1(self, variable_qtgui_chooser_1):
        self.variable_qtgui_chooser_1 = variable_qtgui_chooser_1
        self._variable_qtgui_chooser_1_callback(self.variable_qtgui_chooser_1)
        self.volume_3_lines_0.set_band_0_0(self.variable_qtgui_chooser_1)

    def get_variable_qtgui_chooser(self):
        return self.variable_qtgui_chooser

    def set_variable_qtgui_chooser(self, variable_qtgui_chooser):
        self.variable_qtgui_chooser = variable_qtgui_chooser
        self._variable_qtgui_chooser_callback(self.variable_qtgui_chooser)
        self.blocks_selector_0_0_0.set_input_index(self.variable_qtgui_chooser)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)




def main(top_block_cls=filter_show, options=None):

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
