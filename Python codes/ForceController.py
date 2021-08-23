"""
Project: Robotized mTMS system (Connect2Brain)
Code functions: Force-controlled movements and force compensation for Han's Robot
Author: Minh Duc Pham
Company: Aalto University
Updated: 22/08/2021
"""

#Importing necessary libraries
import serial  # Import serial library for reading Arduino through serial connection
import elfin  # Import robot library (The library file should be in the same folder with this code file)
import time  # Import time library for delay
import numpy as np  # Import numpy library for computations

SERVER_IP   = '169.254.153.251'  # Use this IP when working with the real robot
#SERVER_IP   = '127.0.0.1'  # Use this IP when working with the simulator

# Robot Parameters
PORT_NUMBER = 10003
SIZE = 1024
rbtID = 0
nRbtID = 0
ioIndex = 0

arduinoSerialData = serial.Serial('com11', 9600)  # Port and baud rate config for Arduino

# Han's Robot connection configuration
cobot = elfin.elfin()
cobot.connect(SERVER_IP, PORT_NUMBER, SIZE, rbtID, nRbtID, ioIndex)

cobot.SetOverride(0.05)  # Setting robot's movement speed
forceVal = 0  # Force reading variable

def RobotMoveJ(targetJ):
    """
    This is a function for moving the robot in space coordinates with force-constrained.

    Attributes:
        targetJ(array): [J1, J2, J3, J4, J5, J6]
    """
    time.sleep(1)  # Necessary wait time for Arduino signal retrieval
    targetNow = []
    cobot.SetToolCoordinateMotion(0)  # Set tool coordinate motion (0 = Robot base, 1 = TCP)
    while targetNow != targetJ:
        if (arduinoSerialData.inWaiting()>0):
            myData1 = arduinoSerialData.readline().decode('ascii')  # Reading from Arduino terminal
            myData2 = arduinoSerialData.readline().decode('ascii')  # Reading from Arduino terminal
            forceVal1 = float(myData1)
            forceVal2 = float(myData2)
            print(forceVal1)
            print(forceVal2)
        if forceVal1 < 0.1 and forceVal2 < 0.1:  # When there are no forces
            cobot.MoveJ(targetJ)  # Move to input target
            status = cobot.ReadMoveState()
            targetNow = cobot.ReadAcsActualPos()
        elif forceVal1 > 0.1 or forceVal2 > 0.1:  # When there are forces acting
            cobot.GrpStop()  # Robot motor stops

def RobotMoveL(targetL):
    """
    This is a function for moving the robot in specified angular coordinate position with force-constrained.

    Attributes:
        targetL(array): [X, Y, Z, RX, RY, RZ]
    """
    time.sleep(1)  # Necessary wait time for Arduino signal retrieval
    targetNow = []
    cobot.SetToolCoordinateMotion(0)  # Set tool coordinate motion (0 = Robot base, 1 = TCP)
    while targetNow != targetL:
        if (arduinoSerialData.inWaiting()>0):
            myData1 = arduinoSerialData.readline().decode('ascii')  # Reading from Arduino terminal
            myData2 = arduinoSerialData.readline().decode('ascii')  # Reading from Arduino terminal
            forceVal1 = float(myData1)
            forceVal2 = float(myData2)
            print(forceVal1)
            print(forceVal2)
        if forceVal1 < 0.1 and forceVal2 < 0.1:  # When there are no forces
            cobot.MoveL(targetL)  # Move to input target
            status = cobot.ReadMoveState()
            targetNow = cobot.ReadPcsActualPos()
        elif forceVal1 > 0.1 or forceVal2 > 0.1:  # When there are forces acting
            cobot.GrpStop()  # Robot motor stops

# Initial movements
targetJ = [0.0, 0.0, 90.0, 0.0, 90.0, 0.0]
RobotMoveJ(targetJ)

#forceTemp = 0  # Medium variable to compute forceDif

# Moving to
while True:
    if (arduinoSerialData.inWaiting()>0):
        myData1 = arduinoSerialData.readline().decode('ascii')  # Reading from Arduino terminal
        myData2 = arduinoSerialData.readline().decode('ascii')  # Reading from Arduino terminal
        forceVal1 = float(myData1)
        forceVal2 = float(myData2)

        # Compute forceDif to guess force trending
        #forceDif = forceVal - forceTemp
        #forceTemp = forceVal
        #print(forceVal1)
        #print(forceVal2)

        targetFinal = [525., -404., 544., -135., 6., -156.]  # Destination target
        cobot.SetOverride(0.03)  # Setting robot's movement speed

        if forceVal1 < 0.1 and forceVal2 < 0.1:  # When there are no forces acting
            cobot.SetToolCoordinateMotion(0) # Set tool coordinate motion (0 = Robot base, 1 = TCP)
            print(forceVal1)
            print(forceVal2)
            cobot.MoveL(targetFinal)  # Robot moves to the assigned destination
            print(np.round(cobot.ReadPcsActualPos()))

        elif (forceVal1 > 0.1 or forceVal2 > 0.1) and (np.round(cobot.ReadPcsActualPos()).tolist() != targetFinal):
            cobot.GrpStop()
            #pass

        #if forceVal >= 0.1 and cobot.ReadPcsActualPos() == target2:
        elif (forceVal1 > 0.1 or forceVal2 > 0.1) and (np.round(cobot.ReadPcsActualPos()).tolist() == targetFinal):
            while forceVal1 > 0.1 or forceVal2 > 0.1:  # As long as there are forces acting
                #time.sleep(1)
                cobot.SetToolCoordinateMotion(1)  # Set tool coordinate motion (0 = Robot base, 1 = TCP)
                if (arduinoSerialData.inWaiting()>0):
                    myData1 = arduinoSerialData.readline().decode('ascii')  # Reading from Arduino terminal
                    myData2 = arduinoSerialData.readline().decode('ascii')  # Reading from Arduino terminal
                    forceVal1 = float(myData1)
                    forceVal2 = float(myData2)
                    #forceDif = forceVal - forceTemp
                    #forceTemp = forceVal
                cobot.SetOverride(0.03)  # Setting robot's movement speed
                CompenDistance = [2,0,7]
                cobot.MoveRelL(CompenDistance)  # Robot moves in specified spatial coordinate directional
