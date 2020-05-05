# Defines a patient class to store patient information
class Patient():

	def __init__(self, pt_info):
		self.l_name = pt_info['last name']
		self.f_name = pt_info['first name']
		self.dob = pt_info['dob']
		self.ptid = pt_info['ptid']

	def print_pt_info(self):
		# function to print human readable string that contains
		# a patient's identifying information
		pt_info = ("\nPATIENT INFORMATION:\n"
				   "    Last name  : {}\n"
				   "    First name : {}\n"
				   "    DOB        : {}\n"
				   "    Patient ID : {}\n")
		print(pt_info.format(self.l_name, self.f_name, self.dob, self.ptid))
