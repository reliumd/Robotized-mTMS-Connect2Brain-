import elfin
import serial  # Import Serial Library

SERVER_IP   = '169.254.153.251'
#SERVER_IP   = '192.168.50.85'
#PORT_NUMBER = 10003

SIZE = 1024
rbtID = 0
nRbtID = 0
ioIndex = 0
# for testing without the robot uncomment the following lines
#SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 10003

cobot = elfin.elfin()
cobot.connect(SERVER_IP, PORT_NUMBER, SIZE, rbtID, nRbtID, ioIndex)

cobot.SetOverride(0.1)
#cobot.Electrify()
#cobot.StartMaster()
#target = [206.907,10.231,71.118,-32.317,88.270,26.234]
#target = [-383.915, -83.973, 663.49, -164.976, 41.504, -1.745]
#cobot.MoveJ(target)
cobot.MoveHoming()
#print("done on")

#cobot.MoveHoming()

#print(cobot.ReadPcsActualPos())


#target = [1.5,2.4,3.4,4.7,5.8,6.8]
#a = cobot.MoveL(target)
#print(a)
