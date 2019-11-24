import time
import datetime
import sweep
import patient as pt

PATIENT_NAME = "Maxwell, James"
PATIENT_DOB = "08/03/1986"
PATIENT_ID = "012345"
PATIENT_DATA = pt.Patient(PATIENT_NAME, PATIENT_DOB, PATIENT_ID)

time_stamp = datetime.datetime.now()

# Sampling parameters
NUM_CHANNELS = 8    # Number of channels in sweep
NUM_SAMPLES = 200    # Number of samples per sweep
FS = 20            # Sampling frequency, samples/sec
CHANNEL_LABELS = ["F3C3", "C3O1", "F3T3", "T3O3",
                  "F4C4", "C4O2", "F4T4", "T4O2"]


data = sweep.Sweep(PATIENT_DATA, time_stamp, NUM_CHANNELS,
                   NUM_SAMPLES, FS, CHANNEL_LABELS)

data.print_header()
#while True:
for i in range(NUM_SAMPLES):
    for j in range(NUM_CHANNELS):
        data.set_data(j, i, i)
        time.sleep(1/FS)
    data.print_samples(i)
