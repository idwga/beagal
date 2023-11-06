import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_10", GPIO.IN)
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_12", GPIO.IN)
a = 0
b = 0

while True:
    a = GPIO.input("P8_12")
    b = GPIO.input("P8_10")

    if b == 0:
        GPIO.output("P8_10", GPIO.HIGH)
        time.sleep(1)
    else:
        GPIO.output("P8_10", GPIO.LOW)
        time.sleep(1)
    if a == 1:
        break

