import serial
import time
import configparser
import classes.Sweep as Sweep
import classes.Patient as Patient

# Import information from config file
exec(open("./config.py").read())
config = configparser.ConfigParser()
config.read('config.ini')

# Extract serial connection information and establish link
#serial_info = []
#for key in config['serial']:
#	serial_info.append(config['serial'][key])
#serial_1 = serial.Serial('COM7', baudrate = 115200, timeout = 1)

# Extract patient information and store in a Patient object
pt_info = []
for key in config['patient']:
	pt_info.append(config['patient'][key])
patient = Patient.Patient(pt_info[0], pt_info[1], pt_info[2], pt_info[3])

patient.print_pt_info()


