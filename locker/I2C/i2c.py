"""------------------------------------------------------------*-
  I2C initialize module for Raspberry Pi
  Tested on: Raspberry Pi 3 B+
  (c) Minh-An Dao 2019
  version 1.00 - 10/10/2019
 --------------------------------------------------------------
 *
 *
 --------------------------------------------------------------"""
from smbus2 import SMBus


class I2C_ROOT:
    def __init__(self):
        # -----Open I2C interface:
        # bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
        self.bus = SMBus(1)  # Rev 2 Pi uses 1
