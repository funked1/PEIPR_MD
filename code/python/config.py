import configparser

config = configparser.ConfigParser()

# Configure patient information
config['patient'] = {
					'last' : 'Maxwell',
					'first': 'James',
					'dob'  : '06/13/1831',
					'ptid' : '123-45-6789'
					}

# Configure recording channel names
config['channels'] = {
					 'ch1': 'f3c3',
					 'ch2': 'c3o1',
					 'ch3': 'f3t3',
					 'ch4': 't3o1',
					 'ch5': 'f4c4',
					 'ch6': 'c4o2',
					 'ch7': 'f4t4',
					 'ch8': 't4o2'
					 }


with open('config.ini', 'w') as configfile:
	config.write(configfile)
