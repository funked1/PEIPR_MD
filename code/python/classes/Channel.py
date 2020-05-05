import numpy as np

class Channel():
	def __init__(self, label, num_samples):
		self.label = label
		self.raw_data = np.empty([1, num_samples], dtype=float)
		self.filtered_data = 0
		self.raw_freq_spectrum = 0
		self.freq_spectrum = 0

	def init_filtered_array(self, signal_length):
		self.filtered_data = np.empty([1, signal_length], dtype=float)
