import supervisor
import time
import digitalio
from board import *
import board
from duckyinpython import *
import wifi
from webapp import *
time.sleep(.5)


supervisor.runtime.autoreload = False
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

progStatus = False
progStatus = getProgrammingStatus()
print("progStatus", progStatus)
if(progStatus == False):
    payload = selectPayload()
    runScript(payload)
else:
    print("")

