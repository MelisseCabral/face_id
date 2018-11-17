import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')
labels = {}

with open('labels.pickle', 'rb') as f:
    oglabels = pickle.load(f)
    labels = {v:k for k,v in oglabels.items()}

cap = cv2.VideoCapture(0)
current_img = 0

while (True):
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
        # Recognize
        id_, conf = recognizer.predict(roi_gray)
        if(conf >= 50):
            name = (labels[id_])

            cv2.putText(frame, name, (x, y), font, 1, (255, 255, 255), stroke)
        #img_item = str(current_img) + '.png'
        # current_img += 1
        # cv2.imwrite(img_item, roi_color)

        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    # Display the resulting frame
    cv2.imshow('Recognizer', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()