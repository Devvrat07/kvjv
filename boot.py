from board import *
import board
import digitalio
import storage

noStorage = False
noStoragePin = digitalio.DigitalInOut(GP15)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = noStoragePin.value

if(board.board_id == 'raspberry_pi_pico'):
    noStorage = not noStorageStatus
elif(board.board_id == 'raspberry_pi_pico_w'):

    noStorage = noStorageStatus

if(noStorage == True):
    storage.disable_usb_drive()
    print("Disabling USB drive")
else:
    print("USB drive enabled")

