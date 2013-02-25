from webiopi import runLoop
from webiopi.clients import *
from time import sleep

client = MulticastClient()

gpio = NativeGPIO(client)
gpio.setFunction(25, "out")
state = True

def loop(): 
    global gpio, state
    gpio.output(25, state)
    state = not state
    sleep(0.5)

runLoop(loop)
