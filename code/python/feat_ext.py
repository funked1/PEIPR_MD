from scipy import fft
import numpy as np
from scipy.signal import blackman
import matplotlib.pyplot as plt

def perform_fft(sweep):
    fs = sweep.samp_freq
    num_channels = sweep.num_channels
    num_samples = sweep.num_samples

    T = 1.0/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), num_samples//2)

    for i, channel in enumerate(sweep.channels):
        channel.raw_freq_spectrum = fft(channel.raw_data)
        channel.freq_spectrum = fft(channel.filtered_data)
