import configparser
import classes.Sweep as Sweep

# Import sampling parameters from config file
exec(open("./config.py").read())
config = configparser.ConfigParser()
config.read('config.ini')
