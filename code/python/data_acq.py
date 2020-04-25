import numpy as np

def simulate_serial_read(file_name):
    fp = open(file_name, "r")
    sim_data = fp.readline()
    sim_data = sim_data.encode('ascii', 'strict')
    fp.close()
    return(sim_data)

def sort_signal_data(data_buf, num_samples, num_channels):
    signal_buf = np.empty([num_channels, num_samples], dtype=float)
    idx = 0
    for i in range(num_samples):
        for j in range(num_channels):
            signal_buf[j][i] = float(data_buf[idx])
            idx = idx + 1
    return(signal_buf)
