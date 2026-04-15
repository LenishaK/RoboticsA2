# RoboticsA2
# Automated Bin Transportation Robot 

## 1.	Project overview 
This project focuses on the design and development of an automated robot capable of transporting bins from one location to another. The system uses a VEX EXP robot combined with programmed control logic to stimulate a real-world industrial task. 

The aim of the project is to demonstrate how robotics can be used to automate repetitive tasks such as moving items in environments like warehouses, manufacturing and logistics. The robot is designed to move towards an object, pick it up using a claw mechanism, and transport it to a designated location.

This project highlights how automation can improve efficiency, reduce human effort, and increase consistency in repetitive processes. This system combines both physical robotics and visual sensing to create a more intelligent automated solution. 

# 2.	Problem being solved 
In environments such as warehouses and factories, moving items manually can be physically demanding, inefficient, and time-consuming. When large numbers of items or containers need to be relocated, human involvement can slow processes down and increase labour costs.

This project addresses this issue by creating a robotic system that can:
- move towards a bin
- secure it using a claw mechanism
- transport it to a new location
- release it accurately

This improves efficiency and reduces the need for manual handling. 

# 3.	Hardware used 
The hardware used in this project includes:
- VEX EXP Robot
- Left and right drive motors (for movement)
- Arm motor (for lifting the bin)
- Claw motor (for gripping the bin)
- Raspberry Pi
- Raspberry Pi Camera Module 2

The Raspberry Pi and camera module are used to capture visual input, allowing the system to detect and support decision-making for the robot's actions. 

# 4.	Software used 
The software used in this project includes:
- VEXcode Python - used to program the robot
- Thonny (Raspberry Pi IDE) - used to run Python scripts on the Raspberry Pi
- Python programming language for implementing control logic
- Basic image processing techniques for handling camera input

The Raspberry Pi processes camera data, while the VEX robot carries out the physical actions.

# 5.	Control algorithm 
The robot follows a step-by-step control algorithm to complete the task:
1. Capture an image using the Raspberry Pi camera
2. Process the image to identify the target bin
3. Start with the claw open 
4. Move forward towards the bin
5. Close the claw to grip the bin
6. Lift the arm to secure it
7. Turn towards the drop-off location
8. Move forward to the target area
9. Lower the arm
10. Open the claw to release the bin
11. Reverse and return to the starting position

This algorithm combines both sensor input (camera) and robot movement, allowing the system to perform the task more intelligently.

# 6.	How to run the code 
1. Connect the Raspberry Pi and ensure the camera module is enabled
2. Open Thonny and run the Python script for image capture and processing.
3. Connect the VEX EXP robot to VEXcode Python
4. Upload the robot control program 
5. Power on the robot
6. Run the program

This system will capture an image, identify the bin, and perform the transportation automatically.

# 7. System behaviour
The system works by combining visual input with physical movement. The Raspberry Pi captures an image and processes it to identify the bin. This information is then used to guide the robot's actions. 
The robot follows a fixed sequence of movements to approach, pick up, and transport the bin. The use of both sensing (camera) and control logic allows the system to behave more intelligently compared to simple pre-programmed movement.

This demonstrates how combining sensing and control systems can create a more effective and intelligent robotics solution. 

# 8. Limitations 
There are some limitations within the system: 
- The robot follows pre-defined movements and does not dynamically adjust its path
- Camera detection may be affected by lighting conditions
- Camera also has a slight pink hue, which can affect the outcome 
- The system assumes the bin is placed within a known position
- There is no obstacle avoidance
- The VEX EXP and Raspberry Pi are not directly integrated, meaning decisions from the camera are not automatically sent to the robot. Instead, they operate separately. 

These limitations mean the system works best in a controlled environment.

# 9. Possible improvements 
- Implement obstacle detection using sensors
- Improve camera accuracy using advanced image processing (e.g. OpenCV)
- Add dynamic navigation instead of fixed movements
- Allow the robot to handle multiple bins automatically

These improvements would make the system more efficient and closer to real-world industrial robotics. 

# 10. References 
- VEX Robotics
- Raspberry Pi Documentation
- Python Documentation
- Lecture materials and workshop content
