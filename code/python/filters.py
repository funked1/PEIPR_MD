from scipy import signal

def lpf_40(fs):
    bands = (0, 40, 41, 100)
    desired = (1, 1, 0, 0)
    fir = signal.firls(201, bands, desired, nyq = fs)

    #numtaps = 3
    #f = 40
    #fir = signal.firwin(numtaps, f, pass_zero=False, fs=fs)

    return fir
