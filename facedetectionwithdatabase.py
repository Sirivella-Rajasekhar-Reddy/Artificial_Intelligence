import cv2 #opencv
import os
dataset="AI"
name="Ashok"
path=os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)
(width,height)=(130,100)
alg="haarcascade_frontalface_default.xml" #accessed the model file
haar_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+alg) #loading the model with cv2

cam=cv2.VideoCapture(0) #initializing camera
count=1
while count<31:
    print(count)
    _,img=cam.read() #read the frame from the camera
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting color into gray scale img
    face=haar_cascade.detectMultiScale(grayImg,1.3,4) #get coordinates of face
    for(x,y,w,h) in face: #segregating x,y,w,h.
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        faceonly=grayImg[y:y+h,x:x+w]
        resizeImg=cv2.resize(faceonly,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),resizeImg)
        count+=1
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    if key==27:
        break
print("Image captured successfully")
cam.release()
cv2.destroyAllWindows()
