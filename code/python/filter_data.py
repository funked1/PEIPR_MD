import time
import filters
import numpy as np
from scipy.ndimage import convolve1d
from scipy.signal import lfilter

def apply_filters(sweep):
    fs = sweep.samp_freq
    num_channels = sweep.num_channels
    num_samples = sweep.num_samples
    channel_data = sweep.channels

    # Generate filters
    lp_filter = filters.lpf_40(fs)
    notch_filter = filters.notch_60(fs)
    signal_buf = np.empty([num_channels, num_samples], dtype=float)

    sweep.config_filtered_channels(num_samples)

    # Apply filters to raw channel data
    for i in range(sweep.num_channels):
        unfiltered = channel_data[i].raw_data
        filtered = lfilter(lp_filter, 1.0, unfiltered)
        filtered = lfilter(notch_filter[0], notch_filter[1], filtered)

        signal_buf[i] = filtered

    sweep.set_filtered_channel_data(signal_buf)

    return(sweep)
