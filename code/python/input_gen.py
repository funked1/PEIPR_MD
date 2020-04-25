import numpy as np
import scipy
import matplotlib.pyplot as plt

NUM_CHANNELS = 8
NUM_SAMPLES = 113
SAMPLE_LENGTH = 1 # seconds
TARGET_SNR = 5 #db
MEAN_NOISE = 0
MAINS_FREQ = 60

# Generate 8 sine waves with different frequencies and  a 10 second duration
signals = np.empty([NUM_CHANNELS, NUM_SAMPLES], dtype=float)

t = np.linspace(0, SAMPLE_LENGTH, NUM_SAMPLES)
plot_titles = []
for n in range(1, NUM_CHANNELS + 1):
	# Generate pure sinusoidal signal and calculate power and average power
	s = 10 * np.sin(2 * n * np.pi * t)
	s_power = s ** 2
	s_avg = np.mean(s_power)

	# Remove zeros from sample
	for i in range(NUM_SAMPLES):
		if (s_power[i] == 0):
			s_power[i] = 10 ** -10

	# Convert power signal to dB
	s_db = 10 * np.log10(s_power)
	s_avg_db = 10 * np.log10(s_avg)

	# Generate noise vectors
	noise_avg_db = s_avg_db - TARGET_SNR
	noise_avg_power = 10 ** (noise_avg_db / 10)
	noise = np.random.normal(MEAN_NOISE, np.sqrt(noise_avg_power), NUM_SAMPLES)
	mains_noise = 20 * np.sin(2 * MAINS_FREQ * np.pi * t)

	# add noise vectors to signal
	s = s + noise + mains_noise

	# add signal to list
	signals[n - 1] = s
	title = ("%d Hz" %(n))
	plot_titles.append(title)

# Write signal contents to an text file
np.savetxt("signal_data/input.txt", signals, delimiter=',', fmt=('%1.4f'))

# Plot signals for visualization
fig, axs = plt.subplots(2, 4)
idx = 0
for i in range(2):
	for j in range(4):
		axs[i, j].plot(t, signals[idx])
		axs[i, j].set_title(plot_titles[idx])
		idx = idx + 1

plt.show()
