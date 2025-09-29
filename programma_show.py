#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Programma_show
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from Rever___ import Rever___  # grc-generated hier_block
from ehooo_ import ehooo_  # grc-generated hier_block
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from volume_3_lines import volume_3_lines  # grc-generated hier_block
from volume_8_lines import volume_8_lines  # grc-generated hier_block
import sip



class programma_show(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Programma_show", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Programma_show")
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

        self.settings = Qt.QSettings("GNU Radio", "programma_show")

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
        self.variable_qtgui_chooser_2 = variable_qtgui_chooser_2 = 1
        self.variable_qtgui_chooser_1_0 = variable_qtgui_chooser_1_0 = 0
        self.variable_qtgui_chooser_1 = variable_qtgui_chooser_1 = 0
        self.variable_qtgui_chooser_0_1 = variable_qtgui_chooser_0_1 = 0
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0 = 1
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 0
        self.speed_0 = speed_0 = (-10000)
        self.samp_rate = samp_rate = 32000
        self.delay__ = delay__ = 100
        self.del_ = del_ = 1000
        self.const = const = 0.01
        self.band_1_8 = band_1_8 = 2
        self.band_1_7 = band_1_7 = 2
        self.band_1_6 = band_1_6 = 2
        self.band_1_5 = band_1_5 = 2
        self.band_1_4 = band_1_4 = 2
        self.band_1_3 = band_1_3 = 2
        self.band_1_2 = band_1_2 = 2
        self.band_1_1 = band_1_1 = 2
        self.band_0_2 = band_0_2 = 2
        self.band_0_1 = band_0_1 = 2
        self.band_0_0 = band_0_0 = 2

        ##################################################
        # Blocks
        ##################################################

        # Create the options list
        self._variable_qtgui_chooser_3_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_3_labels = ['0', '1']
        # Create the combo box
        self._variable_qtgui_chooser_3_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_3_tool_bar.addWidget(Qt.QLabel("High" + ": "))
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
        self._variable_qtgui_chooser_2_tool_bar.addWidget(Qt.QLabel("Middle" + ": "))
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
        self._variable_qtgui_chooser_1_0_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_1_0_labels = ['3_lines', '8_lines']
        # Create the combo box
        self._variable_qtgui_chooser_1_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_1_0_tool_bar.addWidget(Qt.QLabel("Chooser_ecva" + ": "))
        self._variable_qtgui_chooser_1_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_1_0_tool_bar.addWidget(self._variable_qtgui_chooser_1_0_combo_box)
        for _label in self._variable_qtgui_chooser_1_0_labels: self._variable_qtgui_chooser_1_0_combo_box.addItem(_label)
        self._variable_qtgui_chooser_1_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_1_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_1_0_options.index(i)))
        self._variable_qtgui_chooser_1_0_callback(self.variable_qtgui_chooser_1_0)
        self._variable_qtgui_chooser_1_0_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_1_0(self._variable_qtgui_chooser_1_0_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_1_0_tool_bar)
        # Create the options list
        self._variable_qtgui_chooser_1_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_1_labels = ['0', '1']
        # Create the combo box
        self._variable_qtgui_chooser_1_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_1_tool_bar.addWidget(Qt.QLabel("Bass" + ": "))
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
        self._variable_qtgui_chooser_0_0_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_0_0_labels = ['Eho', 'Reverb']
        # Create the combo box
        self._variable_qtgui_chooser_0_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_0_0_tool_bar.addWidget(Qt.QLabel("Chooser_audio" + ": "))
        self._variable_qtgui_chooser_0_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_0_0_tool_bar.addWidget(self._variable_qtgui_chooser_0_0_combo_box)
        for _label in self._variable_qtgui_chooser_0_0_labels: self._variable_qtgui_chooser_0_0_combo_box.addItem(_label)
        self._variable_qtgui_chooser_0_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_0_options.index(i)))
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)
        self._variable_qtgui_chooser_0_0_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_0_0(self._variable_qtgui_chooser_0_0_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_0_tool_bar)
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
        self._delay___win = qtgui.RangeWidget(self._delay___range, self.set_delay__, "Eho__", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay___win)
        self._del__range = qtgui.Range(100, 1000, 100, 1000, 200)
        self._del__win = qtgui.RangeWidget(self._del__range, self.set_del_, "Rever___", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._del__win)
        self._const_range = qtgui.Range(0.01, 1, 0.01, 0.01, 200)
        self._const_win = qtgui.RangeWidget(self._const_range, self.set_const, "Costansta", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._const_win)
        self._band_1_8_range = qtgui.Range(0, 10, 1, 2, 200)
        self._band_1_8_win = qtgui.RangeWidget(self._band_1_8_range, self.set_band_1_8, "High_3", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_8_win)
        self._band_1_7_range = qtgui.Range(0, 10, 1, 2, 200)
        self._band_1_7_win = qtgui.RangeWidget(self._band_1_7_range, self.set_band_1_7, "High_2", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_7_win)
        self._band_1_6_range = qtgui.Range(0, 10, 1, 2, 200)
        self._band_1_6_win = qtgui.RangeWidget(self._band_1_6_range, self.set_band_1_6, "High_1", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_6_win)
        self._band_1_5_range = qtgui.Range(0, 10, 1, 2, 200)
        self._band_1_5_win = qtgui.RangeWidget(self._band_1_5_range, self.set_band_1_5, "Middle_3", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_5_win)
        self._band_1_4_range = qtgui.Range(0, 10, 1, 2, 200)
        self._band_1_4_win = qtgui.RangeWidget(self._band_1_4_range, self.set_band_1_4, "Middle_2", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_4_win)
        self._band_1_3_range = qtgui.Range(0, 10, 1, 2, 200)
        self._band_1_3_win = qtgui.RangeWidget(self._band_1_3_range, self.set_band_1_3, "Middle_1", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_3_win)
        self._band_1_2_range = qtgui.Range(0, 10, 1, 2, 200)
        self._band_1_2_win = qtgui.RangeWidget(self._band_1_2_range, self.set_band_1_2, "Bass_2", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_2_win)
        self._band_1_1_range = qtgui.Range(0, 10, 1, 2, 200)
        self._band_1_1_win = qtgui.RangeWidget(self._band_1_1_range, self.set_band_1_1, "Bass_1", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_1_win)
        self._band_0_2_range = qtgui.Range(0, 10, 0.5, 2, 200)
        self._band_0_2_win = qtgui.RangeWidget(self._band_0_2_range, self.set_band_0_2, "High", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_0_2_win)
        self._band_0_1_range = qtgui.Range(0, 10, 0.5, 2, 200)
        self._band_0_1_win = qtgui.RangeWidget(self._band_0_1_range, self.set_band_0_1, "Middle", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_0_1_win)
        self._band_0_0_range = qtgui.Range(0, 10, 0.5, 2, 200)
        self._band_0_0_win = qtgui.RangeWidget(self._band_0_0_range, self.set_band_0_0, "Bass", "dial", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_0_0_win)
        self.volume_8_lines_0 = volume_8_lines(
            band_1_1=band_1_1,
            band_1_2=band_1_2,
            band_1_3=band_1_3,
            band_1_4=band_1_4,
            band_1_5=band_1_5,
            band_1_6=band_1_6,
            band_1_7=band_1_7,
            band_1_8=band_1_8,
            semp_rate_0=32000,
        )
        self.volume_3_lines_0_0 = volume_3_lines(
            band_0_0=variable_qtgui_chooser_1,
            band_0_1=variable_qtgui_chooser_2,
            band_0_2=variable_qtgui_chooser_3,
            samp_rate=32000,
        )
        self.volume_3_lines_0 = volume_3_lines(
            band_0_0=band_0_2,
            band_0_1=band_0_1,
            band_0_2=band_0_0,
            samp_rate=32000,
        )
        # Create the options list
        self._variable_qtgui_chooser_0_1_options = [0, 1]
        # Create the labels list
        self._variable_qtgui_chooser_0_1_labels = ['With effects', 'Without effects']
        # Create the combo box
        self._variable_qtgui_chooser_0_1_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_0_1_tool_bar.addWidget(Qt.QLabel("Chooser_audio" + ": "))
        self._variable_qtgui_chooser_0_1_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_0_1_tool_bar.addWidget(self._variable_qtgui_chooser_0_1_combo_box)
        for _label in self._variable_qtgui_chooser_0_1_labels: self._variable_qtgui_chooser_0_1_combo_box.addItem(_label)
        self._variable_qtgui_chooser_0_1_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_1_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_1_options.index(i)))
        self._variable_qtgui_chooser_0_1_callback(self.variable_qtgui_chooser_0_1)
        self._variable_qtgui_chooser_0_1_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_0_1(self._variable_qtgui_chooser_0_1_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_1_tool_bar)
        self._speed_0_tool_bar = Qt.QToolBar(self)
        self._speed_0_tool_bar.addWidget(Qt.QLabel("Speed" + ": "))
        self._speed_0_line_edit = Qt.QLineEdit(str(self.speed_0))
        self._speed_0_tool_bar.addWidget(self._speed_0_line_edit)
        self._speed_0_line_edit.returnPressed.connect(
            lambda: self.set_speed_0(eng_notation.str_to_num(str(self._speed_0_line_edit.text()))))
        self.top_layout.addWidget(self._speed_0_tool_bar)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            3,
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

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.ehooo_0 = ehooo_(
            delay__=delay__,
        )
        self.blocks_wavfile_source_1 = blocks.wavfile_source('C:\\123\\proba.wav', False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            'C:\\123\\proba1.wav',
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_32,
            False
            )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(32000) * samp_rate) if "auto" == "time" else int(32000), 1) )
        self.blocks_selector_0_0_0_0_0_0 = blocks.selector(gr.sizeof_float*1,variable_qtgui_chooser_1_0,0)
        self.blocks_selector_0_0_0_0_0_0.set_enabled(True)
        self.blocks_selector_0_0_0_0 = blocks.selector(gr.sizeof_float*1,variable_qtgui_chooser_0_0,0)
        self.blocks_selector_0_0_0_0.set_enabled(True)
        self.blocks_selector_0_0_0 = blocks.selector(gr.sizeof_float*1,variable_qtgui_chooser_0,0)
        self.blocks_selector_0_0_0.set_enabled(True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.05)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, (32000*2))
        self.audio_source_0_1 = audio.source(samp_rate, '', True)
        self.audio_sink_0_1 = audio.sink(samp_rate, '', False)
        self.Rever_0 = Rever___(
            const=const,
            del_=del_,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.Rever_0, 0), (self.blocks_selector_0_0_0_0, 1))
        self.connect((self.audio_source_0_1, 0), (self.blocks_selector_0_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_selector_0_0_0_0, 0))
        self.connect((self.blocks_selector_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 2))
        self.connect((self.blocks_selector_0_0_0, 0), (self.volume_3_lines_0, 0))
        self.connect((self.blocks_selector_0_0_0, 0), (self.volume_8_lines_0, 0))
        self.connect((self.blocks_selector_0_0_0_0, 0), (self.audio_sink_0_1, 0))
        self.connect((self.blocks_selector_0_0_0_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_selector_0_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.blocks_selector_0_0_0_0_0_0, 0), (self.volume_3_lines_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_selector_0_0_0, 1))
        self.connect((self.blocks_wavfile_source_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.ehooo_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.volume_3_lines_0, 0), (self.blocks_selector_0_0_0_0_0_0, 0))
        self.connect((self.volume_3_lines_0_0, 0), (self.Rever_0, 0))
        self.connect((self.volume_3_lines_0_0, 0), (self.ehooo_0, 0))
        self.connect((self.volume_3_lines_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.volume_8_lines_0, 0), (self.blocks_selector_0_0_0_0_0_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "programma_show")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_chooser_3(self):
        return self.variable_qtgui_chooser_3

    def set_variable_qtgui_chooser_3(self, variable_qtgui_chooser_3):
        self.variable_qtgui_chooser_3 = variable_qtgui_chooser_3
        self._variable_qtgui_chooser_3_callback(self.variable_qtgui_chooser_3)
        self.volume_3_lines_0_0.set_band_0_2(self.variable_qtgui_chooser_3)

    def get_variable_qtgui_chooser_2(self):
        return self.variable_qtgui_chooser_2

    def set_variable_qtgui_chooser_2(self, variable_qtgui_chooser_2):
        self.variable_qtgui_chooser_2 = variable_qtgui_chooser_2
        self._variable_qtgui_chooser_2_callback(self.variable_qtgui_chooser_2)
        self.volume_3_lines_0_0.set_band_0_1(self.variable_qtgui_chooser_2)

    def get_variable_qtgui_chooser_1_0(self):
        return self.variable_qtgui_chooser_1_0

    def set_variable_qtgui_chooser_1_0(self, variable_qtgui_chooser_1_0):
        self.variable_qtgui_chooser_1_0 = variable_qtgui_chooser_1_0
        self._variable_qtgui_chooser_1_0_callback(self.variable_qtgui_chooser_1_0)
        self.blocks_selector_0_0_0_0_0_0.set_input_index(self.variable_qtgui_chooser_1_0)

    def get_variable_qtgui_chooser_1(self):
        return self.variable_qtgui_chooser_1

    def set_variable_qtgui_chooser_1(self, variable_qtgui_chooser_1):
        self.variable_qtgui_chooser_1 = variable_qtgui_chooser_1
        self._variable_qtgui_chooser_1_callback(self.variable_qtgui_chooser_1)
        self.volume_3_lines_0_0.set_band_0_0(self.variable_qtgui_chooser_1)

    def get_variable_qtgui_chooser_0_1(self):
        return self.variable_qtgui_chooser_0_1

    def set_variable_qtgui_chooser_0_1(self, variable_qtgui_chooser_0_1):
        self.variable_qtgui_chooser_0_1 = variable_qtgui_chooser_0_1
        self._variable_qtgui_chooser_0_1_callback(self.variable_qtgui_chooser_0_1)

    def get_variable_qtgui_chooser_0_0(self):
        return self.variable_qtgui_chooser_0_0

    def set_variable_qtgui_chooser_0_0(self, variable_qtgui_chooser_0_0):
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)
        self.blocks_selector_0_0_0_0.set_input_index(self.variable_qtgui_chooser_0_0)

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self.blocks_selector_0_0_0.set_input_index(self.variable_qtgui_chooser_0)

    def get_speed_0(self):
        return self.speed_0

    def set_speed_0(self, speed_0):
        self.speed_0 = speed_0
        Qt.QMetaObject.invokeMethod(self._speed_0_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.speed_0)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)

    def get_delay__(self):
        return self.delay__

    def set_delay__(self, delay__):
        self.delay__ = delay__
        self.ehooo_0.set_delay__(self.delay__)

    def get_del_(self):
        return self.del_

    def set_del_(self, del_):
        self.del_ = del_
        self.Rever_0.set_del_(self.del_)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.Rever_0.set_const(self.const)

    def get_band_1_8(self):
        return self.band_1_8

    def set_band_1_8(self, band_1_8):
        self.band_1_8 = band_1_8
        self.volume_8_lines_0.set_band_1_8(self.band_1_8)

    def get_band_1_7(self):
        return self.band_1_7

    def set_band_1_7(self, band_1_7):
        self.band_1_7 = band_1_7
        self.volume_8_lines_0.set_band_1_7(self.band_1_7)

    def get_band_1_6(self):
        return self.band_1_6

    def set_band_1_6(self, band_1_6):
        self.band_1_6 = band_1_6
        self.volume_8_lines_0.set_band_1_6(self.band_1_6)

    def get_band_1_5(self):
        return self.band_1_5

    def set_band_1_5(self, band_1_5):
        self.band_1_5 = band_1_5
        self.volume_8_lines_0.set_band_1_5(self.band_1_5)

    def get_band_1_4(self):
        return self.band_1_4

    def set_band_1_4(self, band_1_4):
        self.band_1_4 = band_1_4
        self.volume_8_lines_0.set_band_1_4(self.band_1_4)

    def get_band_1_3(self):
        return self.band_1_3

    def set_band_1_3(self, band_1_3):
        self.band_1_3 = band_1_3
        self.volume_8_lines_0.set_band_1_3(self.band_1_3)

    def get_band_1_2(self):
        return self.band_1_2

    def set_band_1_2(self, band_1_2):
        self.band_1_2 = band_1_2
        self.volume_8_lines_0.set_band_1_2(self.band_1_2)

    def get_band_1_1(self):
        return self.band_1_1

    def set_band_1_1(self, band_1_1):
        self.band_1_1 = band_1_1
        self.volume_8_lines_0.set_band_1_1(self.band_1_1)

    def get_band_0_2(self):
        return self.band_0_2

    def set_band_0_2(self, band_0_2):
        self.band_0_2 = band_0_2
        self.volume_3_lines_0.set_band_0_0(self.band_0_2)

    def get_band_0_1(self):
        return self.band_0_1

    def set_band_0_1(self, band_0_1):
        self.band_0_1 = band_0_1
        self.volume_3_lines_0.set_band_0_1(self.band_0_1)

    def get_band_0_0(self):
        return self.band_0_0

    def set_band_0_0(self, band_0_0):
        self.band_0_0 = band_0_0
        self.volume_3_lines_0.set_band_0_2(self.band_0_0)




def main(top_block_cls=programma_show, options=None):

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
