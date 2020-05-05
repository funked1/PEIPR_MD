from scipy import fft
import numpy as np
from scipy.signal import blackman
import matplotlib.pyplot as plt

def perform_fft(sweep):
    fs = sweep.samp_freq
    num_channels = sweep.num_channels
    num_samples = sweep.num_samples

    w = blackman(num_samples)
    T = 1.0/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), num_samples//2)

    for i, channel in enumerate(sweep.channels):
        channel.raw_freq_spectrum = fft(channel.raw_data)
        channel.freq_spectrum = fft(channel.filtered_data)

    # plot signals
    fig, axs = plt.subplots(8, 2)
    for i, channel in enumerate(sweep.channels):
        axs[i, 0].plot(xf[1:num_samples//2], 2.0/num_samples * np.abs(channel.raw_freq_spectrum[1:num_samples//2]))
        axs[i, 1].plot(xf[1:num_samples//2], 2.0/num_samples * np.abs(channel.freq_spectrum[1:num_samples//2]))
        axs[i, 0].set_xlim([0, 100])
        axs[i, 1].set_xlim([0, 100])

    plt.grid()
    plt.show()
