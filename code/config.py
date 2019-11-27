import configparser

config = configparser.ConfigParser()

# Database connection credentials
config['database'] = {'host': 'localhost',
                      'user': 'root',
                      'pswd': 'Halo4BynhzRp',
                      'data': 'test'}

# Configure patient data
config['patient'] = {'l_name': 'Maxwell',
                     'f_name': 'James',
                     'DOB'   : '06/13/1831',
                     'pt_id' : '123-45-678'}

# Configure sampling parameters
config['sampling'] = {'num_channels': 8,
                      'num_samples' : 2000,
                      'samp_freq'   : 200,
                      'temp_hist'   : 10}

# Configure recording channels
config['channels'] = {'ch1': 'f3c3',
                      'ch2': 'c3o1',
                      'ch3': 'f3t3',
                      'ch4': 't3o1',
                      'ch5': 'f4c4',
                      'ch6': 'c4o2',
                      'ch7': 'f4t4',
                      'ch8': 't4o2'}



with open('config.ini', 'w') as configfile:
    config.write(configfile)
