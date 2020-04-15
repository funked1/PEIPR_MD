# Defines a patient class to store patient information
class Patient():
	def __init__(self, l_name, f_name, dob, ptid):
		self.l_name = l_name
		self.f_name = f_name
		self.dob = dob
		self.ptid = ptid

	def print_pt_info(self):
		# function to print human readable string that contains
		# a patient's identifying information
		pt_info = ("\nPATIENT INFORMATION:\n"
				   "    Last name  : {}\n"
				   "    First name : {}\n"
				   "    DOB        : {}\n"
				   "    Patient ID : {}\n")
		print(pt_info.format(self.l_name, self.f_name, self.dob, self.ptid))
