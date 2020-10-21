# import unittest
# unittest.main('test_ssd1306_display_status')


import unittest

from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C
from ssd1306_display_status import display_status


class TestDisplayStatus(unittest.TestCase):
    def test_display_status_handles_str(self):
        """
        test display_status handles str
        """
        # Setup
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        display = SSD1306_I2C(128, 64, i2c)
        status = 'test string'

        # Calls
        error_check = display_status(status)

        # Asserts
        self.assertIsNone(error_check)

    def test_display_status_handles_int(self):
        """
        test display_status handles int
        """
        # Setup
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        display = SSD1306_I2C(128, 64, i2c)
        status = 10

        # Calls
        error_check = display_status(status)

        # Asserts
        self.assertIsNone(error_check)

    def test_display_status_handles_float(self):
        """
        test display_status handles float
        """
        # Setup
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        display = SSD1306_I2C(128, 64, i2c)
        status = 10.111

        # Calls
        error_check = display_status(status)

        # Asserts
        self.assertIsNone(error_check)