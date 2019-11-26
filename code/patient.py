# Defines a patient class to store patient information
class Patient():
    def __init__(self, last_name, first_name, dob, id):
        self.l_name = last_name
        self.f_name = first_name
        self.dob = dob
        self.id = id

    # this function takes no parameters and prints a neatly formatted string
    # that details the patient's personal information
    def print_data(self):
        pt_info = ("Last name  : {}\n"
                   "First name : {}\n"
                   "DOB        : {}\n"
                   "Patient ID : {}")
        print(pt_info.format(self.l_name, self.f_name, self.dob, self.id))
