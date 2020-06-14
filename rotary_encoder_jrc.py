from RPi import GPIO
from time import sleep
import time


clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT)

counter = 0
clkLastState = GPIO.input(clk)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print(counter)
                clkLastState = clkState
                sleep(0.01)
                while GPIO.input(25)== GPIO.LOW:
                        time.sleep(0.1)
                        if GPIO.input(25)== GPIO.HIGH:
                                print("clicky")
                                time.sleep(0.1)
finally:
        GPIO.cleanup()
