import cv2

"""
Csináljunk egy képet amit fekete-fehér de a közepén vagy benne valahol van az eredeti színes képből
"""

width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

starty = 150
endy = 210
startx = 300
endx = 420
movey = 1
movex = 1

while True:
    ignore, frame = cam.read()

    frameROIBGR = frame[starty:endy, startx:endx]

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameGray = cv2.cvtColor(frameGray, cv2.COLOR_GRAY2BGR)
    cv2.imshow("Teszt", frameROIBGR)
    cv2.moveWindow("Teszt", 730, 0)
    frameGray[starty:endy, startx:endx] = frameROIBGR
    cv2.imshow("BGR", frameGray)
    starty += movey
    endy += movey
    startx += movex
    endx += movex
    if endy == height or starty == 0:
        movey = movey*(-1)
    if startx == 0 or endx == width:
        movex = movex*(-1)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break



cam.release()
cv2.destroyAllWindows()