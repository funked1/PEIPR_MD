import serial
import pickle
import time
import configparser
import os
import multiprocessing
import numpy as np
import filter_data
from classes.Patient import Patient
from classes.Sweep import Sweep

# Import information from config file
exec(open("./config.py").read())
config = configparser.ConfigParser()
config.read('config.ini')

# Configure patient information and store in a Patient object
pt_info = []
for key in config['patient']:
	pt_info.append(config['patient'][key])
PATIENT = Patient(pt_info[0], pt_info[1], pt_info[2], pt_info[3])

# Configure sampling parameters
NUM_CHANNELS = int(config['sampling']['num_channels'])
NUM_SAMPLES  = int(config['sampling']['num_samples'])
SWEEP_LENGTH = int(config['sampling']['sweep_length'])
SAMP_FREQ    = float(config['sampling']['samp_freq'])

# Configure channel names
CH_LABELS = []
for key in config['channels']:
    CH_LABELS.append(config['channels'][key])

# Configure serial connection parameters and establish link w/Arduino
PORT     = config['serial']['port']
BAUDRATE = int(config['serial']['baudrate'])
TIMEOUT  = int(config['serial']['timeout'])
#serial_1 = serial.Serial(PORT, baudrate = BAUDRATE, timeout = TIMEOUT)

# Create signal buffer to hold sorted serial data
signal_buf = np.empty([NUM_CHANNELS, NUM_SAMPLES], dtype=float)

while True:

    # Read serial data from Arduino, decode into string, parse into list
    #serial_in = serial_1.readline()
    #data_buf = serial_in.decode("ascii").split(',')
    #data_buf.pop(len(data_buf - 1)) # remove newline character at end of stream

    # sort data into separate signal vectors
    #index = 0
    #if (len(data_buf) == 9000):
    #    for i in range(NUM_SAMPLES):
    #        for j in range(NUM_CHANNELS):
    #            signal_buf[j][i] = data_buf[index]
    #            index = index + 1

	# Create Sweep object and transfer signal data from buffer to sweep channels
	time_stamp = time.time()
	sweep_data = Sweep(PATIENT, time_stamp, NUM_CHANNELS, NUM_SAMPLES,
					   SAMP_FREQ, CH_LABELS)
	sweep_data.set_channel_data(signal_buf)

	# Serialize sweep data to file, store in unique directory
	dir_name = str(int(time_stamp))
	os.mkdir('../python/signal_data/' + dir_name)
	file_name = "signal_data/" + dir_name + "/unfiltered.p"
	pickle.dump(sweep_data, open(file_name, "wb"))

	### TO DO: ###
	### Create new process to filter data in background
	p = multiprocessing.Process(target=filter_data.apply_lowpass, args=[file_name, SAMP_FREQ])
	p.start()
	### Store filtered data in directory created above


	# for testing, delete later
	print("sweep pickled")
	time.sleep(10)
