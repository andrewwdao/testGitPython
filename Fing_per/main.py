"""------------------------------------------------------------*-
  Peripheral controller for Raspberry Pi
  Manipulate 6 IC 74HC595 using C and Subprocess module
  Tested on: Raspberry Pi 3 B+
  (c) Minh-An Dao 2019
  (C) Yasuhiro Ogino 2019
  version 1.00 - 10/10/2019
 --------------------------------------------------------------
 *
 *
 --------------------------------------------------------------"""
import peripheral as per
import fingerPrint
import time


def main():
    per.init()
    fingerPrint.begin()
    fingerPrint.activate()
    while True:
        fingerBuffer = fingerPrint.check()
        fingCode = fingerBuffer[0]
        fingLocation = fingerBuffer[1]
        if fingCode == "MATCHED":
            if fingLocation == 0:
                per.lock01(per.ON)
            if fingLocation == 2:
                per.lock01(per.OFF)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
