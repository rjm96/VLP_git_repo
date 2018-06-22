import os
import math
import numpy as np
import scipy
import subprocess
import time
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.compat import range
import openpyxl.utils



def make_worksheet(filename):
	
	
	return filename
	
def update_worksheet(filename):
	
	
	return filename

def process_filename(filename)
	output=1

	return output

def read_binary(filename):


	return output


def run_gnuradio(x_var, y_var, filesink, time_length=1):
	#process=subprocess.Popen(["python", "testbed_simulation.py", x_var, y_var])
	#runs gnuradio on a timer
	#Time is in seconds. 
	timeout=1
	start = time.time()
	
	process=subprocess.Popen(["python", "testbed_simulation.py", str(x_var), str(y_var), filesink])
	while (timeout == 1):
		now = time.time()
		if (now-start) > time_length:
			timeout = 0
			process.kill()
	return 0

def vector_to_streams(file_source):
	#converts vector of 15 floats to 15 files of 1 stream
	process = subprocess.Popen(["python", "vector_to_streams.py", file_source])
	time.sleep(3)
	process.kill()
	return file_source
	
def del_binary(directory="/home/rich/Desktop/repos/bin"):
	#removes the binaries from before 
	#makes way for the next binaries
	cwd=os.getcwd()
	os.chdir(directory)
	files = os.listdir(directory)
	for i in files:
		os.remove(i)
	os.chdir(cwd)
	return 0

#TODO
#Loop through X and Y variables
#Run Multilateration on them, write output to Excel
#delete binaries
#keeping the RSSI vectors
def simulate():
	cwd = os.getcwd()
	
	for x in np.arange(0, 3.5, .5):
		for y in np.arange(0,2,.5):
			print x, y
			filesink = cwd+"/RSSI/vlp_simulation_vector_x"+str(x)+"_y"+str(y)+"_.bin"
			print filesink
			
			run_gnuradio( x, y,filesink, 1)
			#RSSI_to_Excel
			vector_to_streams(filesink)
			#Multilateration
			del_binary()
			
	return 0
	
simulate()





