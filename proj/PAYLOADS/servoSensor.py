#!/usr/bin/python2

from gpiozero import LED
import RPi.GPIO as GPIO
import os, signal, subprocess, sys, time, wiringpi

def clockWise():
    """Turn clockwise"""
    p = wpiLoad()
    p.pwmWrite(18, 220)


def counterWise():
    """Turn counter-clockwise"""
    p = wpiLoad()
    p.pwmWrite(18, 80)


def stopWise():
    """Stop previous position"""
    pin = LED(18)
    pin.off()


def wpiLoad():
    # use 'GPIO naming'
    wiringpi.wiringPiSetupGpio()
    
    # set #18 to be a PWM output
    wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
    
    # set the PWM mode to milliseconds stype
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    
    # divide down clock
    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)

    return wiringpi


## Light pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

## Light checks
while True:
    #time.sleep(5)
    if GPIO.input(4) == 1:
        #print 'clockwise'
        clockWise()
    
    if GPIO.input(4) == 0:
        #print 'off/counterwise'
        stopWise()
        #counterWise()
    time.sleep(3)