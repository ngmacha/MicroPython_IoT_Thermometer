# import unittest
# unittest.main('test_mpu6050')


import unittest
from machine import SoftI2C, Pin

from micropython_mpu6050.mpu6050 import MPU6050


class TestMPU6050(unittest.TestCase):
    def test_mpu6050_combine_register_values(self):
        """
        test mpu6050 combine_register_values properly returns a combined 16-bit value
        """
        # Setup
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        mpu6050_int = Pin(14, Pin.IN, Pin.PULL_UP)
        temp_h = b'\x81'
        temp_l = b'\xf0'

        # Instantiate
        mpu = MPU6050(i2c)

        # Calls
        temp_data = mpu.combine_register_values(temp_h, temp_l)

        # Asserts
        self.assertEqual(temp_data, -32272)

    def test_get_temp_data(self):
        """
        test get_temp_data returns a proper value
        """
        # Setup
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        mpu6050_int = Pin(14, Pin.IN, Pin.PULL_UP)

        # Instantiate
        mpu = MPU6050(i2c)

        # Calls
        temp_f = mpu.get_temp_data(i2c)

        # Asserts
        self.assertAlmostEqual(temp_f, 75, delta=10.0)

    def test_get_accel_data(self):
        """
        test get_accel_data returns a proper value
        """
        # Setup
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        mpu6050_int = Pin(14, Pin.IN, Pin.PULL_UP)
        test_accel_data = [0.0078125, -0.006347656, 0.9926758]
        test_accel_data_x = test_accel_data[0]
        test_accel_data_y = test_accel_data[1]
        test_accel_data_z = test_accel_data[2]

        # Instantiate
        mpu = MPU6050(i2c)

        # Calls
        accel_data = mpu.get_accel_data(i2c)
        accel_data_x = accel_data[0]
        accel_data_y = accel_data[1]
        accel_data_z = accel_data[2]

        # Asserts
        self.assertAlmostEqual(accel_data_x, test_accel_data_x, delta=10.0)
        self.assertAlmostEqual(accel_data_y, test_accel_data_y, delta=10.0)
        self.assertAlmostEqual(accel_data_z, test_accel_data_z, delta=10.0)

    def test_get_gyro_data(self):
        """
        test get_gyro_data returns a proper value
        """
        # Setup
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        mpu6050_int = Pin(14, Pin.IN, Pin.PULL_UP)
        test_gyro_data = [3.160305, -0.1068702, 1.343511]
        test_gyro_data_x = test_gyro_data[0]
        test_gyro_data_y = test_gyro_data[1]
        test_gyro_data_z = test_gyro_data[2]

        # Instantiate
        mpu = MPU6050(i2c)

        # Calls
        gyro_data = mpu.get_gyro_data(i2c)
        gyro_data_x = gyro_data[0]
        gyro_data_y = gyro_data[1]
        gyro_data_z = gyro_data[2]

        # Asserts
        self.assertAlmostEqual(gyro_data_x, test_gyro_data_x, delta=10.0)
        self.assertAlmostEqual(gyro_data_y, test_gyro_data_y, delta=10.0)
        self.assertAlmostEqual(gyro_data_z, test_gyro_data_z, delta=10.0)
