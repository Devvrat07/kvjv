
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

    
    wifi.radio.start_ap(secrets['ssid'],secrets['password'])

    HOST = repr(wifi.radio.ipv4_address_ap)
    PORT = 80       
    print(HOST,PORT)


supervisor.runtime.autoreload = False



led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()


progStatus = False
progStatus = getProgrammingStatus()

if(progStatus == False):
   
    payload = selectPayload()

    runScript(payload)

    print("Done")
else:
    print(" ")

led_state = False

async def main_loop():
    global led,button1

    button_task = asyncio.create_task(monitor_buttons(button1))
    if(board.board_id == 'raspberry_pi_pico_w'):
        pico_led_task = asyncio.create_task(blink_pico_w_led(led))
       
        startWiFi()
        
        webservice_task = asyncio.create_task(startWebService())
        await asyncio.gather(pico_led_task, button_task, webservice_task)
    else:
        pico_led_task = asyncio.create_task(blink_pico_led(led))
        await asyncio.gather(pico_led_task, button_task)

asyncio.run(main_loop())
