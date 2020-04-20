import numpy as np
from classes.Patient import Patient
from classes.Sweep import Sweep
from classes.Channel import Channel

# create sweep object to store recorded data
time_stamp = -1
rec_data = Sweep(patient, time_stamp, NUM_CHANNELS, NUM_SAMPLES,
                 SAMP_FREQ, CH_LABELS)


# Generate signal vectors from recorded data
t_axis = np.linspace(0, SAMPLE_LENGTH, NUM_SAMPLES)
signals = np.loadtxt("signal_data/input.txt", dtype=float, delimiter=',')
