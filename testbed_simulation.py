#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SDVLC  Testbed Simulation
# Author: Rich McAllister
# Generated: Tue Jun 19 21:15:19 2018
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from multi_goertzel import multi_goertzel  # grc-generated hier_block
from optparse import OptionParser
from vlp_testbed_sources import vlp_testbed_sources  # grc-generated hier_block
import math
import numpy
import vlp2


class testbed_simulation(gr.top_block):

    def __init__(self, x_var, y_var, filesink):
        gr.top_block.__init__(self, "SDVLC  Testbed Simulation")

        ##################################################
        # Parameters
        ##################################################
        self.CtCr = (1.402589, 1.400153, 1.389144, 1.386729, 1.367899, 1.353108, 1.338055, 1.320068, 1.297516, 1.276457, 1.261740, 1.247866, 1.233018, 1.200908, 1.184429, 1.169045, 1.155984, 1.142038, 1.127352, 1.111633, 1.096738, 1.081336, 1.067067, 1.053066, 1.038244, 1.023078, 1.007937, 0.99301, 0.977535, 0.961326, 0.940293, 0.908008, 0.856049)
        CtCr=self.CtCr
        self.filesink = filesink

        ##################################################
        # Variables
        ##################################################
        self.dZ = dZ = 2.05
        x_var=float(x_var)
        y_var=float(y_var)
        self.y_var = y_var
        self.x_var = x_var
        self.TX_coords = TX_coords = ( (3.62, 1.28, dZ), (3.62, .84, dZ), (3.62, .32, dZ), (2.87, 1.28, dZ), (2.87, .84, dZ), (2.87, .32, dZ), (2.20, 1.28, dZ), (2.2, .84, dZ), (2.2, .32, dZ), (1.48, 1.28, dZ), (1.48, .84, dZ), (1.48, .32, dZ), (.825, 1.32, dZ), (.825, .84, dZ), (.825, .32, dZ) )
        self.distances = distances = ( numpy.sqrt(  (x_var-TX_coords[0][0])**2 + (y_var-TX_coords[0][1])**2 + (dZ**2) ), numpy.sqrt(  (x_var-TX_coords[1][0])**2 + (y_var-TX_coords[1][1])**2 + (dZ**2) ), numpy.sqrt(  (x_var-TX_coords[2][0])**2 + (y_var-TX_coords[2][1])**2 + (dZ**2) ),          numpy.sqrt(  (x_var-TX_coords[3][0])**2 + (y_var-TX_coords[3][1])**2 + (dZ**2) ), numpy.sqrt(  (x_var-TX_coords[4][0])**2 + (y_var-TX_coords[4][1])**2 + (dZ**2) ), numpy.sqrt(  (x_var-TX_coords[5][0])**2 + (y_var-TX_coords[5][1])**2 + (dZ**2) ),
                       numpy.sqrt(  (x_var-TX_coords[6][0])**2 + (y_var-TX_coords[6][1])**2 + (dZ**2) ), numpy.sqrt(  (x_var-TX_coords[7][0])**2 + (y_var-TX_coords[7][1])**2 + (dZ**2) ),numpy.sqrt(  (x_var-TX_coords[8][0])**2 + (y_var-TX_coords[8][1])**2 + (dZ**2) ),            numpy.sqrt(  (x_var-TX_coords[9][0])**2 + (y_var-TX_coords[9][1])**2 + (dZ**2) ),  numpy.sqrt(  (x_var-TX_coords[10][0])**2 + (y_var-TX_coords[10][1])**2 + (dZ**2) ), numpy.sqrt(  (x_var-TX_coords[11][0])**2 + (y_var-TX_coords[11][1])**2 + (dZ**2) ), numpy.sqrt(  (x_var-TX_coords[12][0])**2 + (y_var-TX_coords[12][1])**2 + (dZ**2) ),numpy.sqrt(  (x_var-TX_coords[13][0])**2 + (y_var-TX_coords[13][1])**2 + (dZ**2) ), numpy.sqrt(  (x_var-TX_coords[14][0])**2 + (y_var-TX_coords[14][1])**2 + (dZ**2) )   )
        self.samp_rate = samp_rate = int(2e6)
        self.lam_order = lam_order = .88
        self.goertzel_size = goertzel_size = 2048
        self.angles = angles = ( numpy.arccos(  dZ/distances[0]  )  * (180/math.pi), numpy.arccos(  dZ/distances[1]  )  * (180/math.pi), numpy.arccos(  dZ/distances[2]   ) * (180/math.pi), numpy.arccos(  dZ/distances[3]   ) * (180/math.pi), numpy.arccos(  dZ/distances[4] ) * (180/math.pi), numpy.arccos(  dZ/distances[4]   ) * (180/math.pi), numpy.arccos(  dZ/distances[5] ) * (180/math.pi), numpy.arccos(  dZ/distances[6]   ) * (180/math.pi), numpy.arccos(  dZ/distances[7]  ) * (180/math.pi), numpy.arccos(  dZ/distances[8] ) * (180/math.pi), numpy.arccos(  dZ/distances[9] ) * (180/math.pi), numpy.arccos(  dZ/distances[10] ) * (180/math.pi), numpy.arccos(  dZ/distances[11] ) * (180/math.pi), numpy.arccos(  dZ/distances[12] ) * (180/math.pi), numpy.arccos(  dZ/distances[14] ) * (180/math.pi), numpy.arccos(  dZ/distances[14] ) * (180/math.pi))
        self.TX_freqs = TX_freqs = (1e5, 1.5e5, 2e5,2.5e5,3e5,3.5e5,4e5,4.5e5,5e5, 5.5e5, 6e5, 6.5e5,7e5,7.5e5,8e5)
        self.TX_ampl = TX_ampl = .7

        ##################################################
        # Blocks
        ##################################################
        self.vlp_testbed_sources_0 = vlp_testbed_sources(
            CtCr=CtCr,
            TX_coords=TX_coords,
            TX_freqs=TX_freqs,
            angles=angles,
            dZ=dZ,
            distances=distances,
            lam_order=lam_order,
            noise_ampl=0,
            samp_rate=samp_rate,
            tx_ampl=TX_ampl,
            x_var=x_var,
            y_var=y_var,
        )
        self.vlp2_amp2d_ff_0 = vlp2.amp2d_ff(TX_ampl, dZ, 1, (CtCr), 1, 1, 1.1, 1, 90, 15)
        self.multi_goertzel_0 = multi_goertzel(
            freqs=TX_freqs,
            goertzel_size=goertzel_size,
            mult=2,
            samp_rate=samp_rate,
        )
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_float*1, 15)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*15, self.filesink, False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_streams_to_vector_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.multi_goertzel_0, 0), (self.vlp2_amp2d_ff_0, 0))
        self.connect((self.multi_goertzel_0, 1), (self.vlp2_amp2d_ff_0, 1))
        self.connect((self.multi_goertzel_0, 10), (self.vlp2_amp2d_ff_0, 10))
        self.connect((self.multi_goertzel_0, 11), (self.vlp2_amp2d_ff_0, 11))
        self.connect((self.multi_goertzel_0, 12), (self.vlp2_amp2d_ff_0, 12))
        self.connect((self.multi_goertzel_0, 13), (self.vlp2_amp2d_ff_0, 13))
        self.connect((self.multi_goertzel_0, 14), (self.vlp2_amp2d_ff_0, 14))
        self.connect((self.multi_goertzel_0, 2), (self.vlp2_amp2d_ff_0, 2))
        self.connect((self.multi_goertzel_0, 3), (self.vlp2_amp2d_ff_0, 3))
        self.connect((self.multi_goertzel_0, 4), (self.vlp2_amp2d_ff_0, 4))
        self.connect((self.multi_goertzel_0, 5), (self.vlp2_amp2d_ff_0, 5))
        self.connect((self.multi_goertzel_0, 6), (self.vlp2_amp2d_ff_0, 6))
        self.connect((self.multi_goertzel_0, 7), (self.vlp2_amp2d_ff_0, 7))
        self.connect((self.multi_goertzel_0, 8), (self.vlp2_amp2d_ff_0, 8))
        self.connect((self.multi_goertzel_0, 9), (self.vlp2_amp2d_ff_0, 9))
        self.connect((self.vlp2_amp2d_ff_0, 0), (self.blocks_streams_to_vector_0, 0))
        self.connect((self.vlp2_amp2d_ff_0, 1), (self.blocks_streams_to_vector_0, 1))
        self.connect((self.vlp2_amp2d_ff_0, 10), (self.blocks_streams_to_vector_0, 10))
        self.connect((self.vlp2_amp2d_ff_0, 11), (self.blocks_streams_to_vector_0, 11))
        self.connect((self.vlp2_amp2d_ff_0, 12), (self.blocks_streams_to_vector_0, 12))
        self.connect((self.vlp2_amp2d_ff_0, 13), (self.blocks_streams_to_vector_0, 13))
        self.connect((self.vlp2_amp2d_ff_0, 14), (self.blocks_streams_to_vector_0, 14))
        self.connect((self.vlp2_amp2d_ff_0, 2), (self.blocks_streams_to_vector_0, 2))
        self.connect((self.vlp2_amp2d_ff_0, 3), (self.blocks_streams_to_vector_0, 3))
        self.connect((self.vlp2_amp2d_ff_0, 4), (self.blocks_streams_to_vector_0, 4))
        self.connect((self.vlp2_amp2d_ff_0, 5), (self.blocks_streams_to_vector_0, 5))
        self.connect((self.vlp2_amp2d_ff_0, 6), (self.blocks_streams_to_vector_0, 6))
        self.connect((self.vlp2_amp2d_ff_0, 7), (self.blocks_streams_to_vector_0, 7))
        self.connect((self.vlp2_amp2d_ff_0, 8), (self.blocks_streams_to_vector_0, 8))
        self.connect((self.vlp2_amp2d_ff_0, 9), (self.blocks_streams_to_vector_0, 9))
        self.connect((self.vlp_testbed_sources_0, 0), (self.multi_goertzel_0, 0))

    def get_CtCr(self):
        return self.CtCr

    def set_CtCr(self, CtCr):
        self.CtCr = CtCr
        self.vlp_testbed_sources_0.set_CtCr(self.CtCr)
        self.vlp2_amp2d_ff_0.set_CtCr((self.CtCr), 1, 1, 1.1, 1, 90)

    def get_dZ(self):
        return self.dZ

    def set_dZ(self, dZ):
        self.dZ = dZ
        self.set_distances(( numpy.sqrt(  (self.x_var-self.TX_coords[0][0])**2 + (self.y_var-self.TX_coords[0][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[1][0])**2 + (self.y_var-self.TX_coords[1][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[2][0])**2 + (self.y_var-self.TX_coords[2][1])**2 + (self.dZ**2) ),          numpy.sqrt(  (self.x_var-self.TX_coords[3][0])**2 + (self.y_var-self.TX_coords[3][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[4][0])**2 + (self.y_var-self.TX_coords[4][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[5][0])**2 + (self.y_var-self.TX_coords[5][1])**2 + (self.dZ**2) ),
                       numpy.sqrt(  (self.x_var-self.TX_coords[6][0])**2 + (self.y_var-self.TX_coords[6][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[7][0])**2 + (self.y_var-self.TX_coords[7][1])**2 + (self.dZ**2) ),numpy.sqrt(  (self.x_var-self.TX_coords[8][0])**2 + (self.y_var-self.TX_coords[8][1])**2 + (self.dZ**2) ),            numpy.sqrt(  (self.x_var-self.TX_coords[9][0])**2 + (self.y_var-self.TX_coords[9][1])**2 + (self.dZ**2) ),  numpy.sqrt(  (self.x_var-self.TX_coords[10][0])**2 + (self.y_var-self.TX_coords[10][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[11][0])**2 + (self.y_var-self.TX_coords[11][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[12][0])**2 + (self.y_var-self.TX_coords[12][1])**2 + (self.dZ**2) ),numpy.sqrt(  (self.x_var-self.TX_coords[13][0])**2 + (self.y_var-self.TX_coords[13][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[14][0])**2 + (self.y_var-self.TX_coords[14][1])**2 + (self.dZ**2) )   ))
        self.set_angles(( numpy.arccos(  self.dZ/self.distances[0]  )  * (180/math.pi), numpy.arccos(  self.dZ/self.distances[1]  )  * (180/math.pi), numpy.arccos(  self.dZ/self.distances[2]   ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[3]   ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[4] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[4]   ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[5] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[6]   ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[7]  ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[8] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[9] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[10] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[11] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[12] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[14] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[14] ) * (180/math.pi)))
        self.set_TX_coords(( (3.62, 1.28, self.dZ), (3.62, .84, self.dZ), (3.62, .32, self.dZ), (2.87, 1.28, self.dZ), (2.87, .84, self.dZ), (2.87, .32, self.dZ), (2.20, 1.28, self.dZ), (2.2, .84, self.dZ), (2.2, .32, self.dZ), (1.48, 1.28, self.dZ), (1.48, .84, self.dZ), (1.48, .32, self.dZ), (.825, 1.32, self.dZ), (.825, .84, self.dZ), (.825, .32, self.dZ) ))
        self.vlp_testbed_sources_0.set_dZ(self.dZ)

    def get_y_var(self):
        return self.y_var

    def set_y_var(self, y_var):
        self.y_var = y_var
        self.set_distances(( numpy.sqrt(  (self.x_var-self.TX_coords[0][0])**2 + (self.y_var-self.TX_coords[0][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[1][0])**2 + (self.y_var-self.TX_coords[1][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[2][0])**2 + (self.y_var-self.TX_coords[2][1])**2 + (self.dZ**2) ),          numpy.sqrt(  (self.x_var-self.TX_coords[3][0])**2 + (self.y_var-self.TX_coords[3][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[4][0])**2 + (self.y_var-self.TX_coords[4][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[5][0])**2 + (self.y_var-self.TX_coords[5][1])**2 + (self.dZ**2) ),
                       numpy.sqrt(  (self.x_var-self.TX_coords[6][0])**2 + (self.y_var-self.TX_coords[6][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[7][0])**2 + (self.y_var-self.TX_coords[7][1])**2 + (self.dZ**2) ),numpy.sqrt(  (self.x_var-self.TX_coords[8][0])**2 + (self.y_var-self.TX_coords[8][1])**2 + (self.dZ**2) ),            numpy.sqrt(  (self.x_var-self.TX_coords[9][0])**2 + (self.y_var-self.TX_coords[9][1])**2 + (self.dZ**2) ),  numpy.sqrt(  (self.x_var-self.TX_coords[10][0])**2 + (self.y_var-self.TX_coords[10][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[11][0])**2 + (self.y_var-self.TX_coords[11][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[12][0])**2 + (self.y_var-self.TX_coords[12][1])**2 + (self.dZ**2) ),numpy.sqrt(  (self.x_var-self.TX_coords[13][0])**2 + (self.y_var-self.TX_coords[13][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[14][0])**2 + (self.y_var-self.TX_coords[14][1])**2 + (self.dZ**2) )   ))
        self.vlp_testbed_sources_0.set_y_var(self.y_var)

    def get_x_var(self):
        return self.x_var

    def set_x_var(self, x_var):
        self.x_var = x_var
        self.set_distances(( numpy.sqrt(  (self.x_var-self.TX_coords[0][0])**2 + (self.y_var-self.TX_coords[0][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[1][0])**2 + (self.y_var-self.TX_coords[1][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[2][0])**2 + (self.y_var-self.TX_coords[2][1])**2 + (self.dZ**2) ),          numpy.sqrt(  (self.x_var-self.TX_coords[3][0])**2 + (self.y_var-self.TX_coords[3][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[4][0])**2 + (self.y_var-self.TX_coords[4][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[5][0])**2 + (self.y_var-self.TX_coords[5][1])**2 + (self.dZ**2) ),
                       numpy.sqrt(  (self.x_var-self.TX_coords[6][0])**2 + (self.y_var-self.TX_coords[6][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[7][0])**2 + (self.y_var-self.TX_coords[7][1])**2 + (self.dZ**2) ),numpy.sqrt(  (self.x_var-self.TX_coords[8][0])**2 + (self.y_var-self.TX_coords[8][1])**2 + (self.dZ**2) ),            numpy.sqrt(  (self.x_var-self.TX_coords[9][0])**2 + (self.y_var-self.TX_coords[9][1])**2 + (self.dZ**2) ),  numpy.sqrt(  (self.x_var-self.TX_coords[10][0])**2 + (self.y_var-self.TX_coords[10][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[11][0])**2 + (self.y_var-self.TX_coords[11][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[12][0])**2 + (self.y_var-self.TX_coords[12][1])**2 + (self.dZ**2) ),numpy.sqrt(  (self.x_var-self.TX_coords[13][0])**2 + (self.y_var-self.TX_coords[13][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[14][0])**2 + (self.y_var-self.TX_coords[14][1])**2 + (self.dZ**2) )   ))
        self.vlp_testbed_sources_0.set_x_var(self.x_var)

    def get_TX_coords(self):
        return self.TX_coords

    def set_TX_coords(self, TX_coords):
        self.TX_coords = TX_coords
        self.set_distances(( numpy.sqrt(  (self.x_var-self.TX_coords[0][0])**2 + (self.y_var-self.TX_coords[0][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[1][0])**2 + (self.y_var-self.TX_coords[1][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[2][0])**2 + (self.y_var-self.TX_coords[2][1])**2 + (self.dZ**2) ),          numpy.sqrt(  (self.x_var-self.TX_coords[3][0])**2 + (self.y_var-self.TX_coords[3][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[4][0])**2 + (self.y_var-self.TX_coords[4][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[5][0])**2 + (self.y_var-self.TX_coords[5][1])**2 + (self.dZ**2) ),
                       numpy.sqrt(  (self.x_var-self.TX_coords[6][0])**2 + (self.y_var-self.TX_coords[6][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[7][0])**2 + (self.y_var-self.TX_coords[7][1])**2 + (self.dZ**2) ),numpy.sqrt(  (self.x_var-self.TX_coords[8][0])**2 + (self.y_var-self.TX_coords[8][1])**2 + (self.dZ**2) ),            numpy.sqrt(  (self.x_var-self.TX_coords[9][0])**2 + (self.y_var-self.TX_coords[9][1])**2 + (self.dZ**2) ),  numpy.sqrt(  (self.x_var-self.TX_coords[10][0])**2 + (self.y_var-self.TX_coords[10][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[11][0])**2 + (self.y_var-self.TX_coords[11][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[12][0])**2 + (self.y_var-self.TX_coords[12][1])**2 + (self.dZ**2) ),numpy.sqrt(  (self.x_var-self.TX_coords[13][0])**2 + (self.y_var-self.TX_coords[13][1])**2 + (self.dZ**2) ), numpy.sqrt(  (self.x_var-self.TX_coords[14][0])**2 + (self.y_var-self.TX_coords[14][1])**2 + (self.dZ**2) )   ))
        self.vlp_testbed_sources_0.set_TX_coords(self.TX_coords)

    def get_distances(self):
        return self.distances

    def set_distances(self, distances):
        self.distances = distances
        self.set_angles(( numpy.arccos(  self.dZ/self.distances[0]  )  * (180/math.pi), numpy.arccos(  self.dZ/self.distances[1]  )  * (180/math.pi), numpy.arccos(  self.dZ/self.distances[2]   ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[3]   ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[4] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[4]   ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[5] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[6]   ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[7]  ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[8] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[9] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[10] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[11] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[12] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[14] ) * (180/math.pi), numpy.arccos(  self.dZ/self.distances[14] ) * (180/math.pi)))
        self.vlp_testbed_sources_0.set_distances(self.distances)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.vlp_testbed_sources_0.set_samp_rate(self.samp_rate)
        self.multi_goertzel_0.set_samp_rate(self.samp_rate)

    def get_lam_order(self):
        return self.lam_order

    def set_lam_order(self, lam_order):
        self.lam_order = lam_order
        self.vlp_testbed_sources_0.set_lam_order(self.lam_order)

    def get_goertzel_size(self):
        return self.goertzel_size

    def set_goertzel_size(self, goertzel_size):
        self.goertzel_size = goertzel_size
        self.multi_goertzel_0.set_goertzel_size(self.goertzel_size)

    def get_angles(self):
        return self.angles

    def set_angles(self, angles):
        self.angles = angles
        self.vlp_testbed_sources_0.set_angles(self.angles)

    def get_TX_freqs(self):
        return self.TX_freqs

    def set_TX_freqs(self, TX_freqs):
        self.TX_freqs = TX_freqs
        self.vlp_testbed_sources_0.set_TX_freqs(self.TX_freqs)
        self.multi_goertzel_0.set_freqs(self.TX_freqs)

    def get_TX_ampl(self):
        return self.TX_ampl

    def set_TX_ampl(self, TX_ampl):
        self.TX_ampl = TX_ampl
        self.vlp_testbed_sources_0.set_tx_ampl(self.TX_ampl)
        self.vlp2_amp2d_ff_0.set_Ax(self.TX_ampl)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=testbed_simulation, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(sys.argv[1], sys.argv[2], sys.argv[3])
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
