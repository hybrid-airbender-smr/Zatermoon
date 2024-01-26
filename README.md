# Deltabot Group Silicon project

the robot.py uses it's own library reference from the programming manual [link](https://manual.doosanrobotics.com/help/programming/latest/publish/en_us/programming-manual-v2-10-3-54692282.html)
the robot.py uses pre-determined coordinate and must be use in [drl studio](https://www.homberger-robotica.com/prodotti/homberger-hub/drl-studio/) integrated development enviroment to function properly 



> _In the later stages of development with the Doosan robot, my colleague recommended implementing TCP communication. This approach involves setting up the DRL Studio computer to listen for commands from another computer. The second computer will send the movement commands directly to the DRL Studio computer. This method allows for greater flexibility, such as incorporating external libraries like Python or even OpenCV, thus removing limitations typically associated with the DRL Studio environment._




the vision.py
We use OpenCV's MatchTemplate, and it utilizes images from the MatchTemplate folder. _The challenge we face is to precisely try matching the images. Additionally, taking lighting into account is incredibly difficult_

additional code that uses in the demo 
servermain.py it uses pre-determined orientation and coordinate as well thats alpha-beta-charlie-alpha-beta.

> _We have discovered that using joint coordinates is more reliable for large movements but with disadvantageous curves movement when placing objects. However, employing linear or world coordinates proves to be more accurate for the precise placement of these objects._
