# Robotized-mTMS-Connect2Brain-

> This project serves as the thesis topic for Minh Duc Pham. This project attempts to prototype a very first robotized mTMS system. The robot is controlled by a hybrid position/force controller. This repository only consists of the force controller. For viewing the project as a whole, please visit Renan's repositories [rmatsuda](https://github.com/rmatsuda)

First of all, I would recommend you to read my final thesis file. Then you can follow the README files for installation and how to use the software. Finally you should be able to execute the programs on the robot through the below guidelines. I hope you will find my findings interesting.

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [Installation](#installation)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

The scope of this project is to create a closed-loop force-controlled algorithm and code for a 6 degree-of-freedom (DOF) robot arm which holds the stimulating coils for mTMS system. The robot should move according to the trajectory planning created by Invesalius, and while moving, should stop any time it detects a force acting against the stimulating coils. On top of that, it will compensate for the changes in the forces acting towards it when it reached the destination point, by retracting in the direction of the force vector. 

#### Requirements
To successfully compile and run all parts of the project the following software and environment must be installed and set up:
* Han's Robot software
* Invesalius
* Arduino IDE
* Python-development environment of choice

[Back To The Top](#Robotized-mTMS-Connect2Brain-)

---

## Installation

#### Han's Robot software
* Install Han's Robot software which comes with the manuals (Robot.3.5.417.556 Application file)

#### Invesalius
* Install Invesalius software ([Link to download](https://github.com/invesalius/invesalius3))
    - Invesalius installation guide ([Link to download](https://github.com/invesalius/invesalius3/wiki/Running-InVesalius-3-in-Windows))

#### Arduino IDE
* Install Arduino IDE ([Link to download](https://www.arduino.cc/en/software))

[Back To The Top](#Robotized-mTMS-Connect2Brain-)

---

## How To Use

#### Sensors and Arduino
* Connect the sensors to Arduino according to this diagram
![Sensor-Connections](https://user-images.githubusercontent.com/63422870/130366230-0ed70bcb-d60b-47a6-9a54-abda45ce45dc.png)
* Open the Arduino program named "AnalogRead" in the repository (please check and modify the Serial Monitor baud rate)
* Connect the Arduino to PC
* Double check the port and baud rate values in the Python code as well
* Open the Serial Monitor to make sure that the sensors are reading
* Remember to close the Serial Monitor before running the code

#### Main Program (Python codes)
* Open CMD and change the directory to the folder holds the python codes
* Double check the port and baud rate values in the Python code if there are any
* Execute "home.py" to ensure that the robot is in home position
* Execute "ForceController.py" to run the program


#### Exporting Force Readings
* Run "PythonToExcel.py" individually or embed these lines onto the main program to extract the force readings to Excel files
* The Excel files can subsequently be imported to Matlab for analysis


## References
Information on Connect2Brain (https://www.connecttobrain.eu/)  
Details on the force sensors (https://www.tekscan.com/products-solutions/force-sensors/a401)

[Back To The Top](#Robotized-mTMS-Connect2Brain-)

---

## License

Apache License, Version 2.0

Copyright (c) [2021] [Duc Pham]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[Back To The Top](#Robotized-mTMS-Connect2Brain-)

---

## Author Info

- Github - [reliumd](https://github.com/reliumd)
- LinkedIn - [Minh Duc Pham](https://www.linkedin.com/in/minh-duc-pham-468ba9a8/)  

[Back To The Top](#Robotized-mTMS-Connect2Brain-)
