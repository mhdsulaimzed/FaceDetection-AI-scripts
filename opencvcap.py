import cv2
#Imported os for createing a new directory and to join images in the directory
import os
#For graphical propmpting
import easygui


cam = cv2.VideoCapture(0)
#Initailising the face detection module in opencv library called Cascadeclassifier into face_cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cv2.namedWindow("python face detection app")



counter = 1

#To capture multiple images from the video its runned in a loop
while True:
    ret,frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    

      # This converts our grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces from grayscale frame(gray)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Crop the face region from the frame
        face_image = frame[y:y+h, x:x+w]

        # For Displaying the croped face image
        cv2.imshow('Face Image', face_image)

        if len(faces) > 0:

           #For get a poped up prompt box for entering the name 
            name = easygui.enterbox("Enter the name of the person: ",title="Name Entry")
        
            #Out of capturing 200  faces 100 of them is moved into a directory called Train and the rest 100 to Test
            if counter<=100:
                path = f"train/{name}"
                if not os.path.exists(path):
                    os.makedirs(path)
                img_name = "{}{}.png".format(name,counter)
                img = os.path.join(path,img_name)
                cv2.imwrite(img,face_image)
                print(f"captured and saved to train- {counter}")
            else:
                path = f"test/{name}"
                if not os.path.exists(path):
                    os.makedirs(path)
                img_name = "{}{}.png".format(name,counter)
                img = os.path.join(path,img_name)
                cv2.imwrite(img,face_image)
                print(f"captured and saved to test- {counter}")

            counter +=1
    if counter >200:
        break


cam.release()
