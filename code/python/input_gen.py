import numpy as np
import scipy
import matplotlib.pyplot as plt

NUM_CHANNELS = 8
NUM_SAMPLES = 1125
SAMPLE_LENGTH = 10 # seconds

# Generate 8 sine waves with different frequencies and  a 10 second duration
signals = np.empty([NUM_CHANNELS, NUM_SAMPLES], dtype=float)

t = np.linspace(0, SAMPLE_LENGTH, NUM_SAMPLES)
for n in range(1, NUM_CHANNELS + 1):	
	s = np.sin(2 * n * np.pi * t)		
	signals[n - 1] = s
	

# Write signal contents to an text file
np.savetxt("signal_data/input.txt", signals, delimiter=',', fmt=('%1.4f'))

# Plot signal for visualization
#plt.plot(t, s)
#plt.xlabel('Time (s)')
#plt.ylabel('sin(x)')
#plt.axis('tight')
#plt.show()
