from statistics import harmonic_mean
import cv2
import numpy as np
import face_recognition
import datetime as dt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

#import images:
pathQuery = os.getenv("QUERY_IMAGES")
pathDetected = os.getenv("DETECTED_IMAGES")
cascadeDetector = os.getenv("FACE_CASCADE_DETECTOR")

def loadImagesAndEncode(path):
    known_face_encoding = []
    known_face_names= []
    myList = os.listdir(path)
    #load images and encode names with data
    for cl in myList:
        imgCur = face_recognition.load_image_file(f'{path}/{cl}')
        # print(cl)
        img_encoding = face_recognition.face_encodings(imgCur)
        # print(img_encoding)
        if len(img_encoding)>0:
            known_face_encoding.append(img_encoding[0])
            known_face_names.append(os.path.splitext(cl)[0])
    return known_face_encoding, known_face_names 

def detectFace(frame,known_face_encoding,known_face_names):
    # print("Entra en detectFace")
    # resize for better performance
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    #convert BGR color (from openCV) to RGB color (for face_recognition)
    rgb_small_frame = small_frame[:,:,::-1]
    #find all faces in current frame and encode them
    face_locations= face_recognition.face_locations(rgb_small_frame)
#    print(face_locations)
    if len(face_locations)>0:
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
            #check for matches
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name = "unknown"
            face_distances = face_recognition.face_distance(known_face_encoding,face_encoding)
            # best_match_index = np.argmin(face_distances)
            if len(matches)>0:
                try:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                except:
                    first_match_index= -1
            face_names.append(name)
            # if first_match_index >=0:
            for(top,right,bottom,left),name in zip(face_locations,face_names):
                top*=4
                bottom*=4
                left*=4
                right*=4
                cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255))
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)
    cv2.imshow("Video",frame)
        # saveImage(frame)
        
def saveImage(frame):
    now = dt.datetime.now()
    aux = now.strftime("%Y%m%d%H%M%S")
    cv2.imwrite(f'{pathQuery}/{aux}'+'.png',frame)
        
def assignName(frame,known_faces,known_names):
    rgb_small_frame = frame[:,:,::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    if len(face_locations)>0 :
        top*=4
        bottom*=4
        left*=4
        right*=4
        for(top,right,bottom,left) in face_locations:
            cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
            cv2.imshow('Video',frame)

def assignNewName(fl,frame,known_faces,known_names):
    for(top,right,bottom,left) in fl:
        top*=4
        bottom*=4
        left*=4
        right*=4
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.imshow('Video',frame)

def videoCapture(everyAmount):
    process_frame =0
    delta = datetime.now()+ timedelta(minutes=1)
    known_faces,known_names = loadImagesAndEncode(pathDetected)
    while True:
        ret, frame =video_capture.read()
        process_frame +=  1
        if process_frame > everyAmount :
            process_frame = 0
            detectFace(frame,known_faces,known_names) 
            if datetime.now() > delta :
                # proceso las caras de nuevo.
                known_faces,known_names = loadImagesAndEncode(pathDetected) 

        key = cv2.waitKey(1) & 0xFF #saca la tecla digitada.
        if key == ord('s'):
            print("Guardo imagen")
            saveImage(frame)
        if key == ord('q'):
            break

video_capture = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cascadeDetector)
checkEveryNFrames = int(os.getenv("CHECK_EVERY_N_FRAMES"))
videoCapture(checkEveryNFrames)
video_capture.release()
cv2.destroyAllWindows()