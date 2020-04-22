import time
import filters

def apply_lowpass(filename, fs):
    filter = filters.lpf_40(fs)
    print("filter created")
