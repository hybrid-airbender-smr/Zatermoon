import pyrealsense2 as rs
import numpy as np
import cv2
import matplotlib.pyplot as plt
import socket

# TCP-Client
def connect_to_server(orientation):
    server_host = '192.168.137.40'  # Use the actual robot server IP
    server_port = 2002  # Use the actual robot server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Send vision-related data to the robot server
    vision_data = orientation
    client_socket.send(vision_data.encode('utf-8'))
    client_socket.close()

# Load the first template image
template_path1 = r'C:\Users\Aurelia\OneDrive\Pictures\template3\alpha8.png'
template_name1 = "alpha"
template1 = cv2.imread(template_path1, 0)
w1, h1 = template1.shape[::-1]

# Load the second template image
template_path2 = r'C:\Users\Aurelia\OneDrive\Pictures\template3\beta8.png'
template_name2 = "beta"
template2 = cv2.imread(template_path2, 0)
w2, h2 = template2.shape[::-1]

# Load the third template image
template_path3 = r'C:\Users\Aurelia\OneDrive\Pictures\template3\charlie9.png'
template_name3 = "charlie"
template3 = cv2.imread(template_path3, 0)
w3, h3 = template3.shape[::-1]

# Configure RealSense pipeline
pipe = rs.pipeline()
cfg = rs.config()
cfg.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
profile = pipe.start(cfg)
color_sensor = profile.get_device().first_color_sensor()

# Disable auto exposure
color_sensor.set_option(rs.option.enable_auto_exposure, 0)

# Set fixed exposure value (you may need to adjust this based on your environment)
fixed_exposure_value = 100  # Example value in milliseconds
color_sensor.set_option(rs.option.exposure, fixed_exposure_value)

# Set the region of interest (ROI) to zoom in
roi_x, roi_y, roi_width, roi_height = 200, 100, 400, 300  # Example values, adjust as needed

# Create ORB detector
orb = cv2.ORB_create()

# Initialize the bar chart for displaying the number of matches
templates = [template_name1, template_name2, template_name3]
match_counts = [0, 0, 0]

plt.figure()

# Set a fixed y-axis range for the histogram
plt.ylim(0, 100)  # Adjust the range as needed

while True:
    # Wait for a coherent pair of frames
    frame = pipe.wait_for_frames()
    color_frame = frame.get_color_frame()

    if not color_frame:
        continue

    # Convert RealSense color frame to OpenCV BGR format
    color_image = np.asanyarray(color_frame.get_data())

    # Crop the image to the specified ROI
    color_image_cropped = color_image[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

    # Convert the cropped frame to grayscale for feature matching
    img_gray = cv2.cvtColor(color_image_cropped, cv2.COLOR_BGR2GRAY)

    # Find the keypoints and descriptors with ORB for each template
    kp1, des1 = orb.detectAndCompute(template1, None)
    kp2, des2 = orb.detectAndCompute(template2, None)
    kp3, des3 = orb.detectAndCompute(template3, None)

    # Use BFMatcher to find the best matches for each template
    bf = cv2.BFMatcher()

    matches1 = bf.knnMatch(des1, orb.detectAndCompute(img_gray, None)[1], k=2)
    good_matches1 = [m for m, n in matches1 if m.distance < 0.9 * n.distance]

    matches2 = bf.knnMatch(des2, orb.detectAndCompute(img_gray, None)[1], k=2)
    good_matches2 = [m for m, n in matches2 if m.distance < 0.9 * n.distance]

    matches3 = bf.knnMatch(des3, orb.detectAndCompute(img_gray, None)[1], k=2)
    good_matches3 = [m for m, n in matches3 if m.distance < 0.9 * n.distance]

    # Update the number of matches for each template
    match_counts[0] = len(good_matches1)
    match_counts[1] = len(good_matches2)
    match_counts[2] = len(good_matches3)

    # Choose the template with the most good matches
    max_matches = max(match_counts)
    selected_template = templates[match_counts.index(max_matches)]

    # Assign the selected template to the anchor_orientation variable
    anchor_orientation = selected_template

    # Draw bounding box and add label for the selected template
    if anchor_orientation:
        w, h = (w1, h1) if anchor_orientation == template_name1 else (
            (w2, h2) if anchor_orientation == template_name2 else (w3, h3))
        color = (0, 255, 0) if anchor_orientation == template_name1 else (
            255, 0, 0) if anchor_orientation == template_name2 else (0, 0, 255)

        # Adjust the coordinates back to the original image size
        if anchor_orientation == template_name1:
            pts_original = np.array(
                [pt + np.array([roi_x, roi_y]) for m in good_matches1 for pt in kp1[m.queryIdx].pt],
                dtype=np.int32)
        elif anchor_orientation == template_name2:
            pts_original = np.array(
                [pt + np.array([roi_x, roi_y]) for m in good_matches2 for pt in kp2[m.queryIdx].pt],
                dtype=np.int32)
        else:
            pts_original = np.array(
                [pt + np.array([roi_x, roi_y]) for m in good_matches3 for pt in kp3[m.queryIdx].pt],
                dtype=np.int32)

        # Calculate the bounding box
        rect = cv2.boundingRect(pts_original)
        cv2.rectangle(color_image, rect[0:2], (rect[0] + rect[2], rect[1] + rect[3]), color, 2)
        cv2.putText(color_image, anchor_orientation, (rect[0], rect[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the result
    cv2.imshow('Template Matching', color_image)

    # Send the vision data to the robot server
    if anchor_orientation:
        connect_to_server(anchor_orientation)

    # Clear the previous content of the bar chart
    plt.clf()

    # Display the updated bar chart
    plt.bar(templates, match_counts, color=['green', 'blue', 'red'])
    plt.title('Number of Good Matches for Each Template')
    plt.xlabel('Templates')
    plt.ylabel('Number of Matches')
    plt.draw()
    plt.pause(0.01)

    # Press 'x' in the keyboard to close the window
    if cv2.waitKey(1) == ord('x'):
        break

# Stop the RealSense pipeline and close the OpenCV window
pipe.stop()
cv2.destroyAllWindows()
plt.close()
