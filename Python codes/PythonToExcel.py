"""
This is the Python program to export force readings from sensor to Excel file
The Excel files can be imported to Matlab for necessary analysis
"""

import serial
import elfin
import datetime
import time
import csv


arduinoSerialData = serial.Serial('com11', 9600)
forceVal = 0
time_start = time.time()
time_duration = 300  # In seconds
weight = 200

with open('FlexSen3B200g5mins-9.csv', 'w', newline='') as csvfile:
    field_names = ['Date', 'Time', 'Weight', 'Force']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writerow({'Date': 'Date', 'Time': 'Time', 'Weight': 'Weight', 'Force': 'Force'})

    while time.time() < time_start + time_duration:
        rightnow = datetime.datetime.now()
        if (arduinoSerialData.inWaiting()>0):
            myData = arduinoSerialData.readline().decode('ascii')
            forceVal = float(myData)
            #print(forceVal)
        writer.writerow({'Date': rightnow.strftime("%d/%m/%Y"), 'Time': rightnow.strftime("%H:%M:%S"), 'Weight': weight, 'Force': forceVal})
        time.sleep(1)
