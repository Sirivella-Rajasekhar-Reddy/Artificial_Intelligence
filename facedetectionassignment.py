import cv2 #opencv
alg="haarcascade_frontalface_default.xml" #accessed the model file
haar_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+alg) #loading the model with cv2

cam=cv2.VideoCapture(0) #initializing camera

while True:
    text="No person detected"
    _,img=cam.read() #read the frame from the camera
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting color into gray scale img
    face=haar_cascade.detectMultiScale(grayImg,1.3,5) #get coordinates of face
    for(x,y,w,h) in face: #segregating x,y,w,h.
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="person datected"
    print(text)
    cv2.putText(img,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
