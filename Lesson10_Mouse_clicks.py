import cv2

width = 640
height = 320
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

evt = 0 #Mert amikor belép a while-ba egy if-el kezdődik, de annak még nincs értéke, nincs deklarálva emiatt, error-t ad ki

def mouseClick(event, xPos, yPos, flags, params): #Event - valami történés, pl mi történt az egérrel, megnyomtuk, elengedtük, görgettük, mindnek lesz egy száma és a MouseCallback arra fog hivatkozni
#xPos - az egér pozíciója
#yPos - az egész másik pozíciója
    global evt #Ez azért kell, hogy a while cikluson belül eltudjuk érni, és tudjunk rá hivatkozni
    global pnt
    if event == cv2.EVENT_LBUTTONDOWN: #Lecsekkolja, hogy ez az event történt-e, bal egér gomb lenyomás
        print("Az egér művelet ez volt:,", event)
        print("Ezen a pozícióban", xPos, yPos)
        pnt = (xPos, yPos)
        evt = event
    if event == cv2.EVENT_LBUTTONUP:
        print("Az egér művelet volt", event)
        print("Ezen a pozícióban", xPos, yPos)
        evt = event
    #pnt = (xPos, yPos) #For fun ha húzni akarom a kört
    if event == cv2.EVENT_RBUTTONUP:
        pnt = (xPos, yPos)
        evt = event



cv2.namedWindow("my WEBcam") #Ezzel létrehozunk egy ablakot, hogy a mousecallback működjön, mert amúgy nem működne mert előbb hívtuk meg mint a while loopban létrehoztuk
cv2.setMouseCallback("my WEBcam", mouseClick) #Ezzel megcsináljuk, hogy tudjunk kattintani az egérrel :D
#Bele kell írni, hogy melyik képen szeretnénk, hogy érzékeljen az egér
#Második paraméternek meg meg kell adni, hogy mit csináljon az egérrel


while True:
    ignore, frame = cam.read()
    if evt == 1 or evt == 4:
        cv2.circle(frame, pnt, 25, (255, 0, 0), 2)
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow("my WEBcam", 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()