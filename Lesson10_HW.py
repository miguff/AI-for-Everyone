"""

Csináljunk egy ROI-t úgy, hogy az bal klikkünk legyen a kezdő, bal felső pontja, amikor meg elengedjük legyen a jobb alsó pontja
majd azt a részt egy külön ablakban jelenítsük meh
Ha jobb egér klibb van, akkor tüntessük el
"""

import cv2


evt = 0

#Definiáljuk azt a függvényt amit a setmaousecallbackbe tesszük be
def MouseClick(event, xPos, yPos, flags, params):
    global evt
    global x
    global y
    if event == cv2.EVENT_LBUTTONDOWN:
        x, y = xPos, yPos #1-es
        evt = event
    if event == cv2.EVENT_LBUTTONUP:
        x, y = xPos, yPos #4-es
        evt = event
    if event == cv2.EVENT_RBUTTONDOWN:
        print(event)
        x, y = xPos, yPos
        evt = event #2-es

width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

#Itt csináljuk meg a windowt meg az egér klikkelőt
cv2.namedWindow("my WEBcam")
cv2.setMouseCallback("my WEBcam", MouseClick)

#Itt beállítjuk a paraméter kezdőd
bfelsőx = "a"
bfelsoy = "b"
jalsox = "c"
jalsoy = "d"

while True:
    ignore, frame = cam.read()

    if evt == 1:
        bfelsőx = str(x)
        bfelsoy = str(y)
    if evt == 4:
        jalsox = str(x)
        jalsoy = str(y)
    if bfelsőx.isnumeric() and bfelsoy.isnumeric() and jalsoy.isnumeric() and jalsox.isnumeric():
        #cv2.rectangle(frame, (int(bfelsőx), int(bfelsoy)), (int(jalsox), int(jalsoy)), (255, 0, 0), 1)
        ROI = frame[int(bfelsoy):int(jalsoy), int(bfelsőx):int(jalsox)]
        cv2.imshow("ROI", ROI)
        cv2.moveWindow("ROI", 700, 0)
    if evt == 2:
        cv2.destroyWindow("ROI")
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow("my WEBcam", 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


