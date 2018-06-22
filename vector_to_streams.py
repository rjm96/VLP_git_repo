#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Vector To Streams
# Generated: Fri Dec 15 00:59:55 2017
##################################################

import os
import sys
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class vector_to_streams(gr.top_block):

    def __init__(self, source):
        gr.top_block.__init__(self, "Vector To Streams")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3e6
        self.source=source

        ##################################################
        # Blocks
        ##################################################
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_float*1, 15)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*15, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*15, self.source, False)
        self.blocks_file_sink_0_5 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/testbed_measurements/automation/bin/tx11.bin', False)
        self.blocks_file_sink_0_5.set_unbuffered(False)
        self.blocks_file_sink_0_4_1 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx12.bin', False)
        self.blocks_file_sink_0_4_1.set_unbuffered(False)
        self.blocks_file_sink_0_4_0 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx7.bin', False)
        self.blocks_file_sink_0_4_0.set_unbuffered(False)
        self.blocks_file_sink_0_4 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/tx2.bin', False)
        self.blocks_file_sink_0_4.set_unbuffered(False)
        self.blocks_file_sink_0_3_1 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx13.bin', False)
        self.blocks_file_sink_0_3_1.set_unbuffered(False)
        self.blocks_file_sink_0_3_0 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx8.bin', False)
        self.blocks_file_sink_0_3_0.set_unbuffered(False)
        self.blocks_file_sink_0_3 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx3.bin', False)
        self.blocks_file_sink_0_3.set_unbuffered(False)
        self.blocks_file_sink_0_2_1 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx14.bin', False)
        self.blocks_file_sink_0_2_1.set_unbuffered(False)
        self.blocks_file_sink_0_2_0 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx9.bin', False)
        self.blocks_file_sink_0_2_0.set_unbuffered(False)
        self.blocks_file_sink_0_2 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx4.bin', False)
        self.blocks_file_sink_0_2.set_unbuffered(False)
        self.blocks_file_sink_0_1 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx6.bin', False)
        self.blocks_file_sink_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_1 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx15.bin', False)
        self.blocks_file_sink_0_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx10.bin', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx5.bin', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/home/rich/Desktop/repos/bin/tx1.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_vector_to_streams_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 4), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 9), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 14), (self.blocks_file_sink_0_0_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 5), (self.blocks_file_sink_0_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 3), (self.blocks_file_sink_0_2, 0))
        self.connect((self.blocks_vector_to_streams_0, 8), (self.blocks_file_sink_0_2_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 13), (self.blocks_file_sink_0_2_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 2), (self.blocks_file_sink_0_3, 0))
        self.connect((self.blocks_vector_to_streams_0, 7), (self.blocks_file_sink_0_3_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 12), (self.blocks_file_sink_0_3_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_file_sink_0_4, 0))
        self.connect((self.blocks_vector_to_streams_0, 6), (self.blocks_file_sink_0_4_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 11), (self.blocks_file_sink_0_4_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 10), (self.blocks_file_sink_0_5, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=vector_to_streams, options=None):

    tb = top_block_cls(sys.argv[1])
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
