#!/usr/bin/python2

import RPi.GPIO as GPIO
import os, signal, subprocess, sys, time

def startOutput():
    """Engage output"""
    #os.system('wall startOutput-begin')
    if os.path.isfile(bPID) == True:
        #print 'output already started, found PID'
        return
    #print 'Starting output'
    proc = subprocess.Popen(bCommand,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            shell = True,
                            preexec_fn = os.setsid)
    #print 'PID = ' + str(proc.pid)
    with open(bPID, 'w') as oFile:
        oFile.write(str(proc.pid) + '\n')
    #os.system('wall startOutput-end')


def stopOutput():
    """Disengage output"""
    #os.system('wall stopOutput-begin')
    if os.path.isfile(bPID) != True:
        #print 'output not started, PID not found'
        return
    #print 'stopping output'
    with open(bPID, 'r') as iFile:
        PID = int(iFile.readline())
    #print "PID = " + str(PID)
    os.killpg(PID, signal.SIGTERM)
    os.remove(bPID)
    #os.system('wall stopOutput-end')


## Env setup
bCommand = '/usr/bin/play /root/proj/MUSIC/DangerZone.mp3'
bPID = 'speaker-pid'

## PID checks
if os.path.isfile(bPID):
    os.remove(bPID)

## Light pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

## Light checking
while True:
    time.sleep(3)
    if GPIO.input(4) == 1:
        startOutput()
    
    if GPIO.input(4) == 0:
        stopOutput()
