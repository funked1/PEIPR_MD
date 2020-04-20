import serial
import numpy as np
import time
import configparser
from classes.Patient import Patient

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

signal_buf = np.empty([NUM_CHANNELS, NUM_SAMPLES], dtype=float)
"""
# main loop
while True:

    # Read serial data from Arduino, decode into string, parse into list
    serial_in = serial_1.readline()
    data_buf = serial_in.decode("ascii").split(',')
    data_buf.pop(len(data_buf - 1)) # remove newline character at end of stream

    # sort data into separate signal vectors
    index = 0
    if (len(data_buf) == 9000)
        for i in range(NUM_SAMPLES):
            for j in range(NUM_CHANNELS):
                signal_buf[j][i] = data_buf[index]
                index = index + 1
"""
