import cv2
import os
import webbrowser
import time


gmail="https://mail.google.com/"
youtube="https://www.youtube.com/"
whatsapp="https://web.whatsapp.com/"
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default_classifier.xml") 
  
# frame capture from camera 
def check_face():
    cap = cv2.VideoCapture(0) 
  
# while loop runs if camera is detecting picture. 
    while 1:  
  
    # reading frames
        ret, img = cap.read()  
  
    # gray scale conversion of each frames 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # Detects faces of different sizes in the input image 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print("Number of faces found:",len(faces))

        for(x,y,w,h) in faces:
              cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    
        if len(faces)>0:
            a=input("you want to open youtube, gmail or whatsapp?")
            if a=='g':
                webbrowser.open_new(gmail)
            elif a=='w':
                webbrowser.open_new(whatsapp)
            else:
                webbrowser.open_new(youtube)
            break
        else:
            shutdown=input("You want to shut down")
            if shutdown=='y':
                os.system('shutdown -s')
            else:
                print('Shutdown Aborted')
            break


    # Wait for Esc key to stop 
  
# Close the window 
    cap.release() 
  
# De-allocate any associated memory usage 
    cv2.destroyAllWindows()

check_face()
# check after each 12 seconds
time.sleep(12)
check_face()







    
