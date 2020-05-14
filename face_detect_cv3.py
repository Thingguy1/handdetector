import os
import cv2
import sys
import subprocess
print(sys.version)
def facedetect(img, timestouched):
    try:
        # Get user supplied values
        imagePath = img
        cascPath = "haarcascade_frontalface_default.xml"

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)
        # Read the image
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)
        )
        numOfFaces = len(faces)
        print("Found {0} faces!".format(numOfFaces))
        if numOfFaces == 0:
            os.system("say dont touch your face")
            timestouched = timestouched + 1
            print("you've touched your face {0} times this sitting!".format(timestouched))
        return timestouched
    except:
        return timestouched
def main():
    timestouched = 0
    while True:
        os.popen('ffmpeg -f avfoundation -loglevel quiet -video_size 1280x720 -framerate 30 -i "0" -preset ultrafast -vframes 1 out.jpg >/dev/null 2>&1')
        timestouched = facedetect("out.jpg", timestouched)
        os.system("rm out.jpg >/dev/null 2>&1")
main()
