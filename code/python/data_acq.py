import numpy as np

def simulate_serial_read(file_name):
    fp = open(file_name, "r")
    sim_data = fp.readline()
    sim_data = sim_data.encode('ascii', 'strict')
    fp.close()

    return(sim_data)

def decode_serial_data(serial_in):
    data_buf = serial_in.decode("ascii").split(',')
    data_buf.pop((len(data_buf) - 1)) # remove newline character at end of stream

    return(data_buf)

def sort_signal_data(data_buf, num_samples, num_channels):
    signal_buf = np.empty([num_channels, num_samples], dtype=float)
    idx = 0
    for i in range(num_samples):
        for j in range(num_channels):
            signal_buf[j][i] = float(data_buf[idx])
            idx = idx + 1
    return(signal_buf)
