class Channel():
	def __init__(self, label, length):
		self.label = label
		self.data = [0] * length
	
	def get_sample(self, i):
		return self.data[i]

	def set_sample(self, i, sample):
		self.data[i] = sample
