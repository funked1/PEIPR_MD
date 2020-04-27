from scipy import signal
import numpy as np
from scipy.signal import kaiserord, lfilter, firwin, freqz
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show


def lpf_40(fs):
    bands = (0, 40, 41, 100)
    desired = (1, 1, 0, 0)
    num_taps = 201

    nyq_rate = 80
    width = 5.0 / nyq_rate
    ripple_db = 60
    N, beta = kaiserord(ripple_db, width)
    cutoff_hz = 40
    taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

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

    fir = signal.firls(num_taps, bands, desired, nyq = fs)

    return taps
