#!/usr/bin/env python
from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
from time import sleep
import logging

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 50)

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

app = Flask(__name__)
ask = Ask(app, '/')


def set_angle(angle, duration=.17):
    pwm.start(0)
    if angle == 'left':
        pwm.ChangeDutyCycle(10) # left -90 deg position
    else:
        pwm.ChangeDutyCycle(1) # left -90 deg position
    sleep(duration)    
    pwm.stop()
    

def end():
    pwm.stop()
    GPIO.cleanup()
    
@ask.intent('RobinRotate', mapping={'status': 'status'})
def gpio_control(status):
    print(1)
    set_angle('left', int(status)/1000)
    return statement(f'Rotated for {status} milliseconds')
    
@app.route('/bodge')
def root():
    gpio_control('left')
    return "Hello World"

if __name__ == '__main__':
   app.debug = True
   app.run()  



#sudo python3 servo.py
#./ngrok http -subdomain=robin_rotate 5000
