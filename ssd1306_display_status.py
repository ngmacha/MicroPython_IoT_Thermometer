import time
from machine import SoftI2C, Pin

from ssd1306 import SSD1306_I2C

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
display = SSD1306_I2C(128, 64, i2c)


def display_status(status):
    """Display status function

    Parameters
    ----------
    status : str, int, float
        Variable to be printed in the display

    Returns
    -------
    None
    """
    try:
        display.fill(0)
        display.text(str(status), 0, 0)
        display.show()
        time.sleep(1)
    except:
        return False