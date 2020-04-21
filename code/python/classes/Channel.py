import numpy as np

class Channel():
	def __init__(self, label, num_samples):
		self.label = label
		self.data = np.empty([1, num_samples], dtype=float)
