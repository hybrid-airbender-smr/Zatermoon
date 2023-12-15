import cv2
import os
import time
from datetime import datetime
import tkinter as tk
from threading import Thread

# Function to update the countdown label
def update_countdown():
    global countdown_value
    if countdown_value > 0:
        countdown_label.config(text=f"Capture in {countdown_value} seconds")
        countdown_value -= 1
        root.after(1000, update_countdown)
    else:
        root.destroy()

# Set the camera index
camera_index = 0
range_value = 5  # Adjust the number of captures as needed

# Set the directory to save the images
save_directory = r'C:\Users\Donih\Pictures\burst_picture'

# Create the save directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Open the camera
cap = cv2.VideoCapture(camera_index)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

try:
    # Capture a burst of images
    for i in range(range_value):
        # Reset countdown value for each capture
        countdown_value = 5  # Change this to the desired countdown time

        # Create a Tkinter window for countdown
        root = tk.Tk()
        root.title("Capture Countdown")

        # Create a label for countdown
        countdown_label = tk.Label(root, text=f"Capture in {countdown_value} seconds")
        countdown_label.pack()

        # Start updating the countdown label
        update_countdown()

        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Generate a unique filename using the current date and time
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = os.path.join(save_directory, f'image_{current_time}_{i + 1}.png')

        # Save the image
        cv2.imwrite(filename, frame)

        # Display a message
        print(f"Image {i + 1} captured and saved as {filename}")

        # Close the Tkinter window
        root.destroy()

finally:
    # Release the camera when done
    cap.release()
    cv2.destroyAllWindows()
    print("Camera released.")
