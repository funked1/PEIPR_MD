# Defines a patient class to store patient information
class Patient():
    def __init__(self, last_name, first_name, dob, id):
        self.l_name = last_name
        self.f_name = first_name
        self.dob = dob
        self.id = id


    def print_data(self):
        # function to print neatly formatted string that contains
        # a patient's identifying information
        pt_info = ("Last name  : {}\n"
                   "First name : {}\n"
                   "DOB        : {}\n"
                   "Patient ID : {}")
        print(pt_info.format(self.l_name, self.f_name, self.dob, self.id))
