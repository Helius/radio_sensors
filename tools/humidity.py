#!/usr/bin/python

import serial
import subprocess
import json
import time
import calendar
import sys
import datetime
from subprocess import call

def dht22_handler(Uid, value):
    Humidity = (value[0]*255 + value[1])*0.1
    if (value[2]&0x80):
        Temperature = (value[2]&0x7F)*255 + value[3]
    else:
        Temperature = (value[2]*255 + value[3])*0.1
    print datetime.datetime.now(), "dht22["+ str(Uid) + "] : ", Temperature, "C, ", Humidity, "%"
    # save to DB
#       call(["rrdtool", "update", "/home/eugene/db/climat.rrd", "N:" + str(Temperature) + ":U:" + str(Humidity) + ":U" ])
    #echo_file('climat_log/tempr', Temperature)
    #echo_file('climat_log/humid', Humidity)
    # send to narodmon.ru
    #echo_file('/home/eugene/.narodmon.data/atom/indoor_humidity/value', Humidity)
    #echo_file('/home/eugene/.narodmon.data/atom/indoor_tempr/value', Temperature)
    # update pid value
    #echo_file('/home/eugene/.window_climat_control_pid/real_tempr', Temperature)




def parse_message (line):
    #print line
    try:
        data=json.loads(line)
        for key, value in data.items():
            #print ">", key, value
            if (key == "type"):
                Type = value
            elif (key == "uid"):
                Uid = value
            if (key == "data"):
                Data = value

        if (Type == 1):                 # DHT22 devices
            dht22_handler(Uid, Data)
        else:                           # Unknown sensor
            print "Unknown sensor type"
    
    except Exception as e:
        print 'Parse JSON <'+line+'> failed:', e


# READ MESSAGES FROM THE PORT

ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1)
print("connected to: " + ser.portstr)
while True:
    # Read a line and convert it from b'xxx\r\n' to xxx
    line = ser.readline()
    if line:  # If it isn't a empty line
        parse_message(line)
ser.close()

