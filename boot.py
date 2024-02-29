from board import *
import board
import digitalio
import storage

noStoragePin = digitalio.DigitalInOut(GP15)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorage = noStoragePin.value
