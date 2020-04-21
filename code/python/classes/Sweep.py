from classes.Channel import Channel
from classes.Patient import Patient

class Sweep():

	def __init__(self, pt, ts, num_channels, n, fs, labels):
		self.patient = pt
		self.time_stamp = ts
		self.num_channels = num_channels
		self.num_samples = n
		self.samp_freq = fs
		self.ch_labels = labels
		self.channels = []

		for i in range(self.num_channels):
			self.channels.append(Channel(self.ch_labels[i], self.num_samples))

	def set_channel_data(self, signal_buffer):

		for i in range(self.num_channels):
			self.channels[i].data = signal_buffer[i]
