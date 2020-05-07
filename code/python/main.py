import serial
import pickle
import time
import configparser
import os
import numpy as np
import data_acq
import filter_data
import signal_plot
import feat_ext
from classes.Patient import Patient
from classes.Sweep import Sweep

# Generate SIMULATION data
exec(open("./input_gen.py").read())

# Import information from config file
exec(open("./config.py").read())
config = configparser.ConfigParser()
config.read('config.ini')

# Configure patient information and store in a Patient object
PATIENT = Patient(config['patient'])
PATIENT.print_pt_info()

# Configure sampling parameters
NUM_CHANNELS = int(config['sampling']['num_channels'])
SWEEP_LENGTH = int(config['sampling']['sweep_length'])
SAMP_FREQ    = float(config['sampling']['samp_freq'])
NUM_SAMPLES  = int(SWEEP_LENGTH * SAMP_FREQ)

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

status = True # FOR TESTING
while status:
    time_stamp = time.time()

    # Read serial data from Arduino, decode into string, parse into list
    # serial_in = serial_1.readline()

    # SIMULATE reading data from serial stream by reading data from input.txt
    serial_in = data_acq.simulate_serial_read("signal_data/input.txt")

    # decode and sort input data into channel vectors
    data_buf = data_acq.decode_serial_data(serial_in)
    signal_buf = data_acq.sort_signal_data(data_buf, NUM_SAMPLES, NUM_CHANNELS)

    # Create Sweep object and transfer signal data from buffer to sweep channels
    sweep_data = Sweep(PATIENT, time_stamp, NUM_CHANNELS, NUM_SAMPLES,
                       SAMP_FREQ, CH_LABELS)
    sweep_data.set_raw_channel_data(signal_buf)

    # Filter raw signal data
    sweep_data = filter_data.apply_filters(sweep_data)
    feat_ext.perform_fft(sweep_data)

    # Serialize sweep data to file, store in unique directory
    #dir_name = str(int(time_stamp))
    dir_name = "TEST_RUN/" # FOR SIMULATION
    file_name = "../python/signal_data/" + dir_name
    isFile = os.path.isfile(file_name)
    if (os.path.exists(file_name) == False):
        os.mkdir(file_name)
    file_name = file_name + "sweep_data.p"
    pickle.dump(sweep_data, open(file_name, "wb"))

    # for testing, delete later
    signal_plot.plot_time_signals(sweep_data)
    signal_plot.plot_freq_signals(sweep_data)
    status = False # only run once for simulation purposes
