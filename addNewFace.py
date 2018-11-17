import numpy as np
import cv2
import pickle
import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, 'images')

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

with open('labels.pickle', 'rb') as f:
    oglabels = pickle.load(f)
    labels = {v:k for k,v in oglabels.items()}

def getImages(_label):
    label = _label
    cap = cv2.VideoCapture(0)
    current_img = 0

    dir = image_dir + '/' + label
    os.mkdir(dir)

    while (current_img < 300):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for(x, y, w, h) in faces:
            # (ycoord_start, ycord_end)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            color = (255, 0, 0)
            stroke = 2
            font = cv2.FONT_HERSHEY_SIMPLEX

            img_item = image_dir +'/' + label + '/'+ str(current_img) + '.png'
            current_img += 1
            cv2.imwrite(img_item, roi_color)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()