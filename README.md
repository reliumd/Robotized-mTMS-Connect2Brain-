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

#### Visual Components
* Open Visual Components file named "Layout.vcmx" (under Visual Components folder)
![Layout](https://user-images.githubusercontent.com/63422870/103789610-e54f9f00-5048-11eb-8b9d-be63f795fc88.png)
* Set up OPC UA connection to TwinCAT and UaExpert
![VC2OPCUA](https://user-images.githubusercontent.com/63422870/103790474-eaf9b480-5049-11eb-9fb2-6b972687f026.PNG)
![VC-TwinCAT](https://user-images.githubusercontent.com/63422870/103791345-03b69a00-504b-11eb-8f67-0436d8bd39e2.png)
* Create Variable Pairs with TwinCAT
![Paired variables](https://user-images.githubusercontent.com/63422870/103791580-47a99f00-504b-11eb-9567-86f55389d950.png)
* Run simulation

#### Beckhoff TwinCAT
* See "installationGuide.pdf" in the IoTTask folder for more information
* Open "IotMqttSampleUsingQueue.sln" file (can be found in TwinCAT folder)
* Remember to change your IP address and port info
![IP address and port](https://user-images.githubusercontent.com/63422870/103790988-930f7d80-504a-11eb-8c4f-b2d24ebaedf4.png)

#### Mosquitto (MQTT broker)
See "installationGuide.pdf" in the IoTTask folder for more information

#### UaExpert (OPC UA Client)
Discover the server address in UaExpert. If it cannot detect the server, manually connnect it through the server address "opc.tcp://localhost:51210/UA/VcOpcUaServer"

#### ThingSpeak
* Log in to ThingSpeak
* Create channel and field, ([guide](https://www.youtube.com/watch?v=sBAuexThr30))
* Make private channel and field
* Create Write API Key
* Replace these values of API key in TwinCAT code
![API key](https://user-images.githubusercontent.com/63422870/103790777-52176900-504a-11eb-95b9-58852edecb04.png)

## References
Information on Connect2Brain (https://www.connecttobrain.eu/)  
Arduino products (https://www.arduino.cc/en/Main/Products)
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
