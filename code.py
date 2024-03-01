
import supervisor


import time
import digitalio
from board import *
import board
from duckyinpython import *
import wifi
from webapp import *



time.sleep(.5)

def startWiFi():
    import ipaddress
  
    try:
        from secrets import secrets
    except ImportError:
        
        raise

    print("Connect wifi")
    
    wifi.radio.start_ap(secrets['ssid'],secrets['password'])

    HOST = repr(wifi.radio.ipv4_address_ap)
    PORT = 80       
    print(HOST,PORT)


supervisor.runtime.autoreload = False


led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()


progStatus = False
progStatus = getProgrammingStatus()
print("progStatus", progStatus)
if(progStatus == False):
    print("Finding payload")
    payload = selectPayload()
    print("Running ", payload)
    runScript(payload)

    print("Done")
else:
    print("Update your payload")

led_state = False

async def main_loop():
    global led,button1

    button_task = asyncio.create_task(monitor_buttons(button1))
    
    pico_led_task = asyncio.create_task(blink_pico_w_led(led))
    print("Starting Wifi")   
    startWiFi()
    print("Starting Web Service")
    webservice_task = asyncio.create_task(startWebService())
    await asyncio.gather(pico_led_task, button_task, webservice_task)
   
asyncio.run(main_loop())
