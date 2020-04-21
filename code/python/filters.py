from scipy import signal

def lpf_40(signal, fs):
    bands = (0, 40, 41, 100)
    desired = (1, 1, 0, 0)
    fir = signal.firls(101, bands, desired, fs = fs)
