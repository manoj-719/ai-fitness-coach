import cv2
camera = cv2.VideoCapture(0) #connects to camera 0 means default camera 1 means external 1 cametra

while True:
    success,frame=camera.read() #reads each frame of the camera
    #succces is used tocheck whter done or nor
    if not success:
        print("could not access")
        break
    cv2.imshow("camera test",frame) #sows the camera in windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllwindows()
