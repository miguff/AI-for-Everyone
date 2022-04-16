import cv2

"""

Nem akarjuk minidg az egészet egyben kezelni, mert nagy proccessing powert igénylehet, emiatt csak egy adott
részre koncentrálunk


-Lehet szín, forma alapján csinálni kijelölni azt a régiót ami kell nekünk és használni fogunk
"""

width = 640
height = 320
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

#Ezek itt az alapbeállítások, amikket célszerű kezdeni, beállítani milyen codec legyen amivel visszajátsza, mekkora legyen, milyen FPS szám legyen

while True:

    ignore, frame = cam.read()
    frameROI=frame[150:210, 250:390] #Ez az eredeti képnek a közepén kiszeüdn egy részt és azt vizsgáljuk
    """
    Itt eltudjuk kezdeni analizálni
    -Tegyük grayscale-lé
    """
    frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROIBGR = cv2.cvtColor(frameROIGray, cv2.COLOR_GRAY2BGR) #Ez visszarakja színesbe, de mivel a szürke az szürke színesben is, mivel elveszítjuk a színeket az előző kóddal
    #cv2.imshow("my GrayROI", frameROIGray)
    #cv2.moveWindow("my GrayROI", 650, 90) #Ha ki van kommentelve akkor performance reason miatt

    #frame[150:210, 250:390] = frameROIGray #Az eredeti képnek a kijelölt részét áttesszük fekete fehérré, ennyi nem elég mert nem egy shape-ben vannak
    frame[150:210, 250:390] = frameROIBGR #Na ez itt most működik, itt nyilván máshova is belehetne tenni, de olyankor a középső kép is menne vele, mivel mindig a középső részt veszi kiL


    #cv2.imshow("my ROI", frameROI)
    #cv2.moveWindow("my ROI", 650, 0)
    cv2.imshow("Teszt", frame)  #Ezeket most szépen kikapcsolom mert nagyon eszi a pi-t :D
    cv2.moveWindow("Teszt", 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()