import configparser
import pymysql
import data_storage as ds

# Import connection credentials and connect to database
config = configparser.ConfigParser()
config.read('config.ini')
dbc = []
for key in config['database']:
    dbc.append(config['database'][key])
#db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])
#cursor = db.cursor()
db = pymysql.connect(host='localhost', user='testuser', password='password', db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

# Construct database architecture:
history_length = 10     # number of minutes to store data
ds.reset_tables(cursor, history_length)
