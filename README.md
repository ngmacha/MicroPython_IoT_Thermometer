![image](https://github.com/mytechnotalent/MicroPython_IoT_Thermometer/blob/main/MicroPython%20IoT%20Thermometer.png?raw=true)

# MicroPython IoT Thermometer
A fun IoT Thermometer which uses an MPU6050 temperature, accelerometer and gyroscope sensor which interfaces with the Adafruit IO in the cloud!

## Schematic
![image](https://github.com/mytechnotalent/MicroPython_IoT_Thermometer/blob/main/schematic.png?raw=true)

## Parts
[ESP32 Development Board](https://www.amazon.com/MELIFE-Development-Dual-Mode-Microcontroller-Integrated/dp/B07Q576VWZ)<br>
[Adafruit MPU-6050 6-DoF Accel and Gyro Sensor - STEMMA QT Qwiic](https://www.adafruit.com/product/3886)

## Installation
```bash
git clone https://github.com/mytechnotalent/MicroPython_IoT_Thermometer.git
```

## Adafruit IO Tutorial
Take a few minutes and read through the Adafruit IO setup to get your device setup and ready.<br>
[Adafruit IO Tutorial](https://learn.adafruit.com/welcome-to-adafruit-io/what-is-adafruit-io)

## Setup pyboard.py Utility
#### SOURCE 
```bash
https://github.com/micropython/micropython/blob/master/tools/pyboard.py
```

#### INSTRUCTIONS
```bash
https://docs.micropython.org/en/latest/reference/pyboard.py.html#running-a-command-on-the-device
```

#### EXAMPLE
```bash
python3 pyboard.py --device <DEVICE> -f cp <FILE> :
```

## Copy Files To MicroPython Device
```bash
unittest.py [SOURCE: https://github.com/micropython/micropython-lib/blob/master/unittest/unittest.py]
config.py
main.py 
mqtt_as [SOURCE: https://github.com/peterhinch/micropython-mqtt/tree/master/mqtt_as]
mpu6050 [SOURCE: https://github.com/mytechnotalent/MicroPython_MPU6050]
ssd1306.py [SOURCE: https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py]
ssd1306_display_status.py
test_ssd1306_display_status.py
```

## Run Tests in REPL
```bash
import unittest
unittest.main('test_ssd1306_display_status')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
