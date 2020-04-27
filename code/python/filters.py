from scipy import signal
import numpy as np
from scipy.signal import kaiserord, lfilter, firwin, freqz
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show
import matplotlib.pyplot as plt

def lpf_40(fs):
    width = 5.0 / fs
    ripple_db = 60
    N, beta = kaiserord(ripple_db, width)
    cutoff_hz = 30
    taps = firwin(N, cutoff_hz, window=('kaiser', beta), fs=fs)

    #--------------------------------------------------------------------------
    # Plot magnitude response of the filter
    #--------------------------------------------------------------------------
    #figure(1)
    #clf()
    #w, h = freqz(taps, worN=8000)
    #plot((w/np.pi)*fs, np.absolute(h), linewidth=2)
    #xlabel('Frequency (Hz)')
    #ylabel('Gain')
    #title('Frequency Response')
    #ylim(-0.05, 1.05)
    #grid(True)

    #show()

    return taps

def notch_50(fs):
    f0 = 50.0 # Frequency to be removed
    Q = 30.0
    zeros, poles = signal.iirnotch(f0, Q, fs)

    #--------------------------------------------------------------------------
    # Plot magnitude response of the filter
    #--------------------------------------------------------------------------
    #freq, h = signal.freqz(zeros, poles, fs=fs)  # frequency response
    #h_db = 20 * np.log10(abs(h))
    #fig, ax = plt.subplots()
    #ax.plot(freq, h_db, color='green')
    #ax.set_title('Frequency Response')
    #ax.set_ylabel('Amplitude (dB)', color='green')
    #ax.set_xlabel('Frequency (Hz)')
    #ax.set_xlim([0, 100])
    #ax.set_ylim([-25, 10])
    #ax.grid()
    #plt.show()

    return [zeros, poles]
