import configparser
import pymysql
import data_storage as ds
import patient as pt
import sweep
import time
import datetime
import RPi.GPIO as GPIO
import mux_ctrl
import board
import digitalio
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import timeit
import csv

# Setup GPIO pins for MUX control signals
mux_1 = digitalio.DigitalInOut(board.D17)
mux_2 = digitalio.DigitalInOut(board.D27)
mux_3 = digitalio.DigitalInOut(board.D22)
mux_1.direction = digitalio.Direction.OUTPUT
mux_2.direction = digitalio.Direction.OUTPUT
mux_3.direction = digitalio.Direction.OUTPUT

# Create I2C bus, define sampling parameters, and create ADC object
i2c = busio.I2C(board.SCL, board.SDA)
GAIN = 1
RATE = 1600
adc = ADS.ADS1015(i2c, gain=GAIN, data_rate=RATE)
chan = AnalogIn(adc, ADS.P0)

# Import connection credentials and connect to database
exec(open("./config.py").read())
config = configparser.ConfigParser()
config.read('config.ini')
db = pymysql.connect(host        = config['database']['host'],
                     user        = config['database']['user'],
                     password    = config['database']['pswd'],
                     db          = config['database']['data'],
                     charset     = config['database']['charset'],
                     cursorclass = pymysql.cursors.DictCursor)
cursor = db.cursor()

# Construct empty database
exec(open("./db_setup.py").read())

# Import patient information and store it in a patient object
# pt_info = [l_name, f_name, dob, pt_id]
pt_info = []
for key in config['patient']:
    pt_info.append(config['patient'][key])
patient = pt.Patient(pt_info[0], pt_info[1], pt_info[2], pt_info[3])

# Import sampling parameters from configuration file
# sp_info = [num_channels, num_samples, sampling_freq, hist_length]
sp_info = []
for key in config['sampling']:
    sp_info.append(int(config['sampling'][key]))

# Add channel entries to channels db
channel_labels = []
for key in config['channels']:
    channel_labels.append(config['channels'][key])
for label in channel_labels:
    ds.insert_channel(db, cursor, label)

# Create sweep object to store sampling data
data = sweep.Sweep(patient, datetime.datetime.now(), sp_info[0],
                   sp_info[1], sp_info[2], channel_labels)

data.print_header()
#period = 1/200 #(sp_info[2]*1.1)
while True:
    start = timeit.default_timer()
    for n in range(sp_info[3]):
        table_n = "data_{}".format(n)
        for i in range(900): #(int(sp_info[1])):
            for j in range(4): #(int(sp_info[0])):
                mux_ctrl.mux_ctrl(j, mux_1, mux_2, mux_3)
                data.set_data(j, i, chan.voltage)
        
        file = "data_{}.csv".format(n)
        with open(file, 'w', newline='') as f:
           writer = csv.writer(f)
           writer.writerow(data.channels[0].data)
    stop = timeit.default_timer()
    print('Sweep Time: {} seconds '.format( stop-start))
