import numpy as np
import scipy
import matplotlib.pyplot as plt

# Sampling Paramters
NUM_CHANNELS = 8
SAMPLE_FREQ = 200	# samples per second
SWEEP_LENGTH = 10   # seconds
NUM_SAMPLES = SAMPLE_FREQ * SWEEP_LENGTH

# Noise characteristics
TARGET_SNR = 2	 #db
MEAN_NOISE = 0
MAINS_FREQ = 60


# Generate 8 sine waves with different frequencies and  a 10 second duration
signals = np.empty([NUM_CHANNELS, NUM_SAMPLES], dtype=float)

t = np.linspace(0, SWEEP_LENGTH, NUM_SAMPLES)
plot_titles = []
for n in range(1, NUM_CHANNELS + 1):
	# Generate pure sinusoidal signal and calculate power and average power
	s = 2.5 * np.sin(2 * n * np.pi * t)
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
	mains_noise = 30 * np.sin(2 * MAINS_FREQ * np.pi * t)

	# add noise vectors to signal
	s = s + noise + mains_noise

	# add signal to list
	signals[n - 1] = s
	title = ("%d Hz" %(n))
	plot_titles.append(title)

# Write signal contents to an text file
fp = open(r"signal_data/input.txt", "w")
idx = 0
for n in range(NUM_SAMPLES):
	for i in range(NUM_CHANNELS):
		buf = ("%1.4f, " % signals[i][n])
		fp.write(buf)
		idx = idx + 1
fp.write("\n")
fp.close()
