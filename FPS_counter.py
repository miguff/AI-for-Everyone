import numpy as np
import cv2
import time

print("Your OpenCV version is: " + cv2.__version__)
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 0, 0)
thickness = 1
old_time = 0
new_time = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    new_time = time.time()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    fps = 1/(new_time-old_time)
    old_time = new_time
    fps = int(fps)
    fps = str(fps)
    cv2.putText(gray, fps, (30, 30), font, 1, color, thickness)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
