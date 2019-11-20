
class Sweep():
    def __init__(self, pt, ts, num_channels, N, Fs, labels):
        self.patient = pt
        self.time_stamp = ts
        self.num_channels = num_channels
        self.num_samples = N
        self.sampling_frequency = Fs
        self.channel_labels = labels
        self.channels = []

        self.set_start_date(self.time_stamp)
        self.set_start_time(self.time_stamp)

        for i in range(self.num_channels):
            self.channels.append(Channel(self.channel_labels[i], self.num_samples))

    def set_start_date(self, time_stamp):
        year = time_stamp.year
        month = time_stamp.month
        day = time_stamp.day
        self.start_date = "{0}/{1}/{2}".format(month, day, year)

    def set_start_time(self, time_stamp):
        hour = time_stamp.hour
        minute = time_stamp.minute
        second = time_stamp.second
        self.start_time = "{}:{}:{}".format(hour, minute, second)

    def set_data(self, channel_num, i, sample):
        self.channels[channel_num].set_sample_value(i, sample)

    def print_header(self):
        column_head = "{: ^20}" * self.num_channels
        fields = ["Patient Name:", "DOB:", "Patient ID:",
                  "Start Date:", "Start Time:"]
        values = [self.patient.name, self.patient.dob,
                  self.patient.id, self.start_date,
                  self.start_time]
        print("-" * 160)
        for i in range(len(fields)):
            print("{:<15} {:<15}".format(fields[i], values[i]))
        print("-" * 160)
        print(column_head.format(*self.channel_labels))

    def print_samples(self, i):
        columns = "{: ^20}" * self.num_channels
        values = []
        for j in range(self.num_channels):
            values.append(self.channels[j].get_sample(i))
        print(columns.format(*values))


class Channel():
    def __init__(self, label, length):
        self.channel_label = label
        self.data = [0]*length

    def get_label(self):
        return self.channel_label

    def get_sample(self, i):
        return self.data[i]

    def set_sample_value(self, i, sample):
        self.data[i] = sample
