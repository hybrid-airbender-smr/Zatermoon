import cv2
import numpy as np
import pyrealsense2 as rs

# RealSense setup
pipe = rs.pipeline()
cfg = rs.config()
cfg.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
cfg.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipe.start(cfg)

while True:
    # RealSense capture
    frame = pipe.wait_for_frames()
    depth_frame = frame.get_depth_frame()
    color_frame = frame.get_color_frame()

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.5), cv2.COLORMAP_JET)

    # Circle detection on the color image from the RealSense camera
    resized_image = cv2.resize(color_image, (500, 500))
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 150, param1=90, param2=60, minRadius=0, maxRadius=0)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw circles on the original resized image
            cv2.circle(resized_image, (i[0], i[1]), i[2], (0, 255, 0), 6)
            cv2.circle(resized_image, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Display the result
    cv2.imshow("Circle Detection", resized_image)
    
    # Press 'x' in keyboard to close windows
    if cv2.waitKey(1) == ord('x'):
        break

# Cleanup
pipe.stop()
cv2.destroyAllWindows()
