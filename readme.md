# Face Detection and Capture using OpenCV

This Python script captures and saves face images using OpenCV's face detection module. It detects faces in a video stream from a webcam and saves the cropped face images to separate directories for training and testing.

This script is designed to perform face detection and capture face images from a video feed. Here's a breakdown of the code documentation:
# Steps
1.Import the necessary libraries:

        cv2 for computer vision and image processing functions.
        os for interacting with the operating system (creating directories, joining file paths).
        easygui for graphical prompting.

2.Initialize the video capture:

        cam = cv2.VideoCapture(0) opens the default camera.


3.Initialize the Haar cascade classifier for face detection:

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') loads the Haar cascade classifier XML file.

4.Create a window for displaying the face detection application:

        cv2.namedWindow("python face detection app") creates a named window.

5.Set up variables for capturing face images:

        counter = 1 is used to count the number of captured face images.

6.Start capturing face images from the video feed:

        Enter a loop that reads frames from the video feed using cam.read().
        Convert each frame to grayscale using cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).
        Detect faces in the grayscale frame using face_cascade.detectMultiScale().
        converting in grayscale makes the face detection easier and time effiecient

7.For each detected face:

        Crop the face region from the frame.
        Display the cropped face image in a separate window using cv2.imshow().
        Prompt the user to enter the name of the person using easygui.enterbox().

8.Save the captured face image to the appropriate directory based on the counter value:

        If counter is less than or equal to 100, save to the train directory.
        If counter is greater than 100, save to the test directory.
        Increment the counter.

9.Check if 200 face images have been captured:

If counter is greater than 200, break the loop.
Release the video capture using cam.release().

This script allows you to capture face images, categorize them into training and testing sets, and save them in separate directories based on the entered name.


