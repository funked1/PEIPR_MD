import numpy as np
import matplotlib.pyplot as plt

def plot_time_signals(sweep):

    if (len(sweep.channels) > 0):
        length_uf = len(sweep.channels[0].raw_data)
        length_f  = len(sweep.channels[0].filtered_data)
        duration = length_uf / sweep.samp_freq

    # obtain signal data from sweep object
    signals_uf = np.empty([sweep.num_channels, length_uf], dtype=float)
    signals_f = np.empty([sweep.num_channels, length_f], dtype=float)

    for i, channel in enumerate(sweep.channels):
        signals_uf[i] = channel.raw_data
        signals_f[i] = channel.filtered_data

    # create time axes
    t_uf = np.linspace(0, duration, length_uf)
    t_f = np.linspace(0, duration, length_f)

    # Plot signals
    fig, axs = plt.subplots(8, 2)
    for i, channel in enumerate(sweep.channels):
        axs[i, 0].plot(t_uf, signals_uf[i])
        axs[i, 1].plot(t_f, signals_f[i])

    plt.show()
