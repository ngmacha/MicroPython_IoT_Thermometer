# config.py Local configuration for mqtt_as demo programs
from sys import platform
from mqtt_as import config

config['server'] = 'io.adafruit.com'  # Change to suit

# Not needed if you're only using ESP8266
config['ssid'] = 'YOUR_SSID'
config['wifi_pw'] = 'YOUR_PASSWORD'

# MQTT params
config['port'] = 8883
config['user'] = 'YOUR_AIO_USERNAME'
config['password'] = 'YOUR_AIO_KEY'
config['keepalive'] = 60
config['ping_interval'] = 30
config['ssl'] = True
config['response_time'] = 10
config['clean_init'] = True
config['clean'] = False
config['max_repubs'] = 4