# RoboticsA2
# Automated Bin Transportation Robot 

## 1.	Project overview 
This project focuses on the design and development of an automated robotcapable of transporting bins from one location to another. The system uses a VEX EXP robot combined with programmed control logic to stimulate a real-world industrial task. 

The aim of the project is to demonstrate how robotics can be used to automate repetitive tasks such as moving items in enviornments like warehouses, manufacturing and logistics. The robot is designed to move towards an object, pick it up using a claw mechanism, and transport it to a designated location.

This project highlights how automation can improve efficiency, reduce human effort and increase consistency in repetitive processes.

# 2.	Problem being solved 
In enviornments such as warehouses and factories, moving items manually can be phsyically demanding, inefficient, and time-consuming. When large numbers of items or containers need to be relocated, human involvement can slow process down and increase labour costs.

this project addresses this issue by creating a robotic system that can:
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

The raspberry Pi and camera module are used to capture visual input, allowing the system to detect and support decision-making for the robot's actions. 

# 4.	Software used 
The software used in thsi project includes:
- VEXcode Python - used to program the robot
- Thonny(Raspberry Pi IDE) - used to run Python scripts on the Raspberry Pi
- Python Programming language for implementing control logic
- Basic image processing techniques for handling camera input

The raspberry Pi processes camera data, while the VEX robot carries out the physical actions.

# 5.	Control algorithm 
The robot follows a step-by-step control algorithm to complete the task:
1. capture an image using the Raspberry Pi camera
2. Process the image to identify the target bin
3. Start with claw open 
4. Move forward towards the bin
5. Close the claw to grip the bin
6. Lift the arm to secure it
7. Turn towards the drop-off location
8. Move forward to the target area
9. Lower the arm
10. Open the claw to release the bin
11. Reverse and return to the starting position

This agorithm combines both sensor input (camera) and robot movement, allowing the system to perform the task more intelligently.

# 6.	How to run the code 
# 7.	References 
# 8.	AI transparency statement 
