import configparser
import pymysql
import data_storage as ds
import patient as pt
import sweep
#import time
import datetime
#import timeit

# Import connection credentials and connect to database
# db_info = [host, user, pw, database]
exec(open("./config.py").read())
config = configparser.ConfigParser()
config.read('config.ini')
db_info = []
for key in config['database']:
    db_info.append(config['database'][key])
#db = pymysql.connect(db_info[0], db_info[1], db_info[2], db_info[3])
db = pymysql.connect(host='localhost',user='testuser',password='password',db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
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
# sp_info = [num_channels, num_samples, sampling_frequency]
sp_info = []
for key in config['sampling']:
    sp_info.append(int(config['sampling'][key]))

# Add channel entries to channels db
channel_labels = []
for key in config['channels']:
    channel_labels.append(config['channels'][key])
for label in channel_labels:
    ds.insert_channel(db, cursor, label)

#time_stamp = datetime.datetime.now()
data = sweep.Sweep(patient, datetime.datetime.now(), sp_info[0],
                   sp_info[1], sp_info[2], channel_labels)

data.print_header()
#table_index = 0;
#while True:
#    apd = "_{}".format(table_index)
#    table_n = TABLES[1] + apd
#    ds.make_table(cursor, table_n, TABLES[1])
#    start = timeit.default_timer()
#    for i in range(NUM_SAMPLES):
#        for j in range(NUM_CHANNELS):
#            data.set_data(j, i, i)
            #ds.insert_sample(db, cursor, table_n, i, j + 1)
            #time.sleep(1/FS)
            #data.print_samples(i)
#    stop = timeit.default_timer()
#    print('Time: ', stop-start)
#
#    table_index = table_index + 1
