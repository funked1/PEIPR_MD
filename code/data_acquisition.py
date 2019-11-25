import time
import datetime
import pymysql
import sweep
import data_storage as ds
import patient as pt
import timeit

# DB connection parameters
HOST = "localhost"
USER = "root"
ROOT_PW = "Halo4BynhzRp"
DATABASE = "test"
TABLES = ["channels", "data"]

# Open DB and instantiate cursor object
db = pymysql.connect(HOST, USER, ROOT_PW, DATABASE)
cursor = db.cursor()

# delete old tables
for table in reversed(TABLES):
    ds.clear_table(cursor, table)

# create new tables
for table in TABLES:
    ds.make_table(cursor, table, table)

PATIENT_NAME = "Maxwell, James"
PATIENT_DOB = "08/03/1986"
PATIENT_ID = "012345"
PATIENT_DATA = pt.Patient(PATIENT_NAME, PATIENT_DOB, PATIENT_ID)

time_stamp = datetime.datetime.now()

# Sampling parameters
NUM_CHANNELS = 8    # Number of channels in sweep
NUM_SAMPLES = 2000   # Number of samples per sweep
FS = 1600             # Sampling frequency, samples/sec

# Add channel entries to channels db
channel_labels = ["F3C3", "C3O1", "F3T3", "T3O3",
                  "F4C4", "C4O2", "F4T4", "T4O2"]
for label in channel_labels:
    ds.insert_channel(db, cursor, label)

data = sweep.Sweep(PATIENT_DATA, time_stamp, NUM_CHANNELS,
                   NUM_SAMPLES, FS, channel_labels)

data.print_header()
table_index = 0;
while True:
    apd = "_{}".format(table_index)
    table_n = TABLES[1] + apd
    ds.make_table(cursor, table_n, TABLES[1])
    start = timeit.default_timer()
    for i in range(NUM_SAMPLES):
        for j in range(NUM_CHANNELS):
            #data.set_data(j, i, i)
            ds.insert_sample(db, cursor, table_n, i, j + 1)
            #   time.sleep(1/FS)
            #data.print_samples(i)
    stop = timeit.default_timer()
    print('Time: ', stop-start)

    table_index = table_index + 1
