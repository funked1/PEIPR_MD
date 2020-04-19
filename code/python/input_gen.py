import numpy as np
import scipy
import matplotlib.pyplot as plt

# Generate a 4Hz sine wave with a 10 second duration
t = np.linspace(0, 10, 1125)
s = np.sin(8 * np.pi * t)

# Write signal contents to an text file
np.savetxt("signal_data/input.txt", s, fmt=('%1.3f'))

# Plot signal for visualization
#plt.plot(t, s)
#plt.xlabel('Time (s)')
#plt.ylabel('sin(x)')
#plt.axis('tight')
#plt.show()
