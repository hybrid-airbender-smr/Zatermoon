from vision import anchor_orientation, template_name1, template_name2, template_name3
import socket
import struct

def tcp_server():
    # Create a TCP/IP socket
    server_host = '192.168.137.40'
    server_port = 2002

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)

    print(f"Robot server listening on {server_host}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        try:
            print(f"Connection established with {client_address}")

            # Receive data from the vision client
            vision_data = client_socket.recv(1024).decode('utf-8')
            print(f"Received vision data: {vision_data}")

            # Process the vision data and perform robot movement
            # (Replace the following line with your actual robot movement logic)
            # perform_robot_movement(vision_data)

            # Send a response back to the vision client if needed
            response_data = "Acknowledgment from robot"
            client_socket.send(response_data.encode('utf-8'))

        finally:
            print("Connection closed.")
            client_socket.close()


if __name__ == "__main__":
    # Start the robot server
    tcp_server()

# HOME Coordinates
home = (posj(82.9, 15.7, -122.5, 2.1, -74.1, 52.1)) # home position

# Stud Coordinates
stud1_top = (posj(127.0, -11.9, -111.0, -3.8, -60.1, 6.4)) # top of the stud1
stud1_grab = (posx(222.6, -311.4, 189.5, 5.8, -175.8, -117.5)) # grab stud
stud2_top = (posx(216.5, -320.0, 229, 55.1, -175.7, -60.5)) #stud2 top
stud2_grab = (posx(216.5, -320.0, 187.1, 55.1, -175.7, -60.5))
stud3_top = (posx(214.6, -338.8, 229, 50.1, -175.5, -63.9)) #stud3 top
stud3_grab = (posx(214.6, -338.8, 189.1, 50.1, -175.5, -63.9))
stud4_top = (posx(213.1, -358.1, 229, 56.2, -175.4, -56.0)) # stud4 top
stud4_grab = (posx(213.1, -358.1, 187.8, 56.2, -175.4, -56.0))
stud5_top = (posx(210.5, -375.4, 229.0, 67.0, -175.5, -43.2)) # stud5 top
stud5_grab = (posx(210.5, -375.4, 187.0, 67.0, -175.5, -43.2))

# Movement per Orientation
def move_alpha ():
    movej(posj(98.6, -59.2, -6.9, -4.7, -133.0, 68.6), v=80, a=100)  # top of speedhex
    movel(posx(81.0, -623.0, 341.0, 110.6, 159.4, 82.2), v=100, a=100)  # grab the speed hex
    movej(posj(98.5, -46.1, -34.2, -5.1, -120.2, 68.6), v=80, a=100)  # top of speedhex
    movej(posj(98.0, -21.5, -75.1, -2.2, -70.3, 68.6), v=80, a=100) #waypoint 1

def move_beta ():
    movej(posj(100.2, -46.3, -35.9, -1.9, -121.6, -56.6), v=80, a=100)  # top of speedhex
    movel(posx(103.3, -598.0, 351.6, 103.5, 153.1, -52.6), v=100, a=100)  # grab the speed hex
    movej(posj(100.2, -46.3, -35.9, -1.9, -121.6, -56.6), v=80, a=100)  # top of speedhex
    movej(posj(122.2, 9.0, -94.2, -2.2, -100.6, -101.4), v=80, a=100) #waypoint 2

def move_charlie ():
    movej(posj(99.5, -38.6, -47.9, -9.3, -110.3, 193.7), v=80, a=100)  # top of speedhex
    movel(posx(73.0, -582.5, 359.7, 127.7, 157.4, -147.2), v=100, a=100)  # grab the speed hex
    movej(posj(97.5, -23.6, -65.0, -8.3, -90.8, 182.2), v=80, a=100)  # top of speedhex
    movej(posj(101.0, -13.5, -73.8, -8.4, -118.5, 182.2), v=80, a=100)  #waypoint 3


# turn it off
set_digital_output(1, 0)
set_digital_output(2, 0)
wait(0.5)

# Picking Up STUD
movej(posj(127.0, -11.9, -111.0, -3.8, -60.1, 6.4), v=80, a=100)# top of the stud
movel(posx(222.6, -311.4, 189.5, 5.8, -175.8, -117.5), v=100, a=100) # grab the stud
set_digital_output(1, 1) # gripper on
wait(2)
movel(posx(226.4, -312.8, 229.5, 175.1, 175.5, 52.5), v=100, a=100) # top of the stud


# Placing STUD in Machine
movej(posj(157.0, -50.5, -17.4, 1.5, -115.5, 40.8), v=80, a=100)  # the front of the machine
movel(posx(597.4, -250.3, 427.0, 135.0, 176.3, 18.2), v=100, a=100) # the top of the machine
movel(posx(598.5, -250.7, 373.4, 135.1, 176.3, 18.2), v=100, a=100) # release the stud in the machine
set_digital_output(1, 0) # gripper off
wait(1)
movej(posj(100.2, -46.3, -35.9, -1.9, -121.6, -56.6), v=80, a=100) # the top of the machine
movel(posx(577.8, -235.3, 418.7, 140.6, 176.8, 23.1), v=100, a=100) # the front of the machine

# Robot Go to HOME
movej(home)

# Codes for SPEEDHEX
if anchor_orientation == template_name1:
    # BETA Orientations
    move_beta()

elif anchor_orientation == template_name2:
    # ALPHA Orientations
    move_alpha()

elif anchor_orientation == template_name3:
    # CHARLIE Orientations
    move_charlie()

else:
    breakpoint()

# Placing SPEEDHEX to Machine
movej(posj(158.3, -43.0, -29.0, -1.5, -106.2, -142.8), v=80, a=100) # front of machine speedhex
movel(posx(589.5, -246.8, 372.1, 103.1, 179.0, 163.4), v=25, a=100) #speedhex release
set_digital_output(1, 0) # gripper off
wait(1)
movel(posx(595.1, -248.3, 373.4, 90.6, 179.3, 150.8), v=25, a=100) #trick release speedhex
movel(posx(588.3, -243.4, 415.2, 168.0, -179.1, -132.1), v=100, a=100)
set_digital_output(2, 1) # rivet machine on

# Robot Go to HOME
movel(home)

