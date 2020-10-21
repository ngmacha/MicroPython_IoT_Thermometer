from machine import SoftI2C, Pin
import network, time

import uasyncio as asyncio
from micropython_mpu6050.mpu6050 import MPU6050
from mqtt_as import MQTTClient
from config import config
from ssd1306_display_status import display_status

# Application is to auto-run on power-up it can be necessary to add a short delay
time.sleep(5)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mpu6050_int = Pin(14, Pin.IN, Pin.PULL_UP)
mqtt_led = Pin(2, Pin.OUT)
mpu = MPU6050(i2c)

SERVER = 'io.adafruit.com'


def callback(topic, msg, retained):
    """Callback function to print topic, msg, retained

    Parameters
    ----------
    topic : str
        Topic
    msg : str
        Msg
    retained : bool
        Retained flag

    Returns
    -------
    None
    """
    print((topic, msg, retained))


async def conn_han(client):
    """ASYNC function to handle connection

    Parameters
    ----------
    client : <class 'MQTTClient'>
        Instance of the MQTTClient class

    Returns
    -------
    None
    """
    await client.subscribe('YOUR_AIO_USERNAME/feeds/sensors.temperature', 1)


async def main(client):
    """ASYNC function main routine

    Parameters
    ----------
    client : <class 'MQTTClient'>
        Instance of the MQTTClient class

    Returns
    -------
    None
    """
    mqtt_led.off()
    await client.connect()
    mqtt_led.on()
    n = 0
    while True:
        await asyncio.sleep(5)
        display_status('publish')
        print('publish', n)
        # If WiFi is down the following will pause for the duration
        reading = mpu.get_temp_data(i2c)
        display_status(reading)
        await client.publish('YOUR_AIO_USERNAME/feeds/sensors.temperature', str(reading), qos=1)
        n += 1


while True:
    config['subs_cb'] = callback
    config['connect_coro'] = conn_han
    config['server'] = SERVER

    MQTTClient.DEBUG = True  # Optional: print diagnostic messages
    client = MQTTClient(config)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(client))
    except KeyboardInterrupt:
        client.close()  # Prevent LmacRxBlk:1 errors
        break
    except Exception as e:
        # An RuntimeError in addition to other errors can occur if you lose 
        # internet so reset the device
        print(e)
        print('Exception')
        client.close()  # Prevent LmacRxBlk:1 errors
        import machine
        machine.reset()
    