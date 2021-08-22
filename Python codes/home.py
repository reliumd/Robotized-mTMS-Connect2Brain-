import elfin  # Import robot library (The library file should be in the same folder with this code file)

SERVER_IP   = '169.254.153.251'  # Use this IP when working with the real robot
#SERVER_IP   = '127.0.0.1'  # Use this IP when working with the simulator

# Robot Parameters
SIZE = 1024
rbtID = 0
nRbtID = 0
ioIndex = 0
PORT_NUMBER = 10003

# Han's Robot connection configuration
cobot = elfin.elfin()
cobot.connect(SERVER_IP, PORT_NUMBER, SIZE, rbtID, nRbtID, ioIndex)

cobot.SetOverride(0.1)  # Setting robot's movement speed

cobot.MoveHoming()  # Robot moves to home position
