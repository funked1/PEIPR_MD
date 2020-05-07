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
    fig, axs = plt.subplots(8, 2, sharex=True, sharey=False)
    fig.suptitle('Time Domain Signals:\nUnfiltered (left), Filtered(right)', fontsize=15, fontweight='bold')
    for i, channel in enumerate(sweep.channels):
        axs[i, 0].plot(t_uf, signals_uf[i])
        ylabel = ("%d Hz" %(i + 1))
        axs[i, 0].set_ylabel(ylabel, fontsize='12', fontweight='bold', rotation='0')
        axs[i, 1].plot(t_f, signals_f[i])

    fig.text(0.5, 0.03, "Time (s)", fontsize='15', fontweight='bold', ha='center')
    plt.show()

def plot_freq_signals(sweep):
    fs = sweep.samp_freq
    num_channels = sweep.num_channels
    num_samples = sweep.num_samples

    T = 1.0/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), num_samples//2)

    # plot signals
    fig, axs = plt.subplots(8, 2, sharex=True, sharey=False)
    fig.suptitle('Frequency Domain Signals:\nUnfiltered (left), Filtered(right)', fontsize=15, fontweight='bold')
    for i, channel in enumerate(sweep.channels):
        axs[i, 0].plot(xf[1:num_samples//2], 2.0/num_samples * np.abs(channel.raw_freq_spectrum[1:num_samples//2]))
        axs[i, 1].plot(xf[1:num_samples//2], 2.0/num_samples * np.abs(channel.freq_spectrum[1:num_samples//2]))
        ylabel = ("%d Hz" %(i + 1))
        axs[i, 0].set_ylabel(ylabel, fontsize='12', fontweight='bold', rotation='0')
        axs[i, 0].set_xlim([0, 80])
        axs[i, 1].set_xlim([0, 80])

    fig.text(0.5, 0.03, "Frequency (Hz)", fontsize='15', fontweight='bold', ha='center')
    plt.show()
