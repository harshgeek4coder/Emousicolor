import cv2
from IPython.display import display, Javascript
from js2py import eval_js
from base64 import b64decode

cascPath = 'haarcascade_frontalface_dataset.xml'  # dataset
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # 0 for web camera live stream

def camera_stream():
     # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame in browser
    return cv2.imencode('.jpg', frame)[1].tobytes()

    

