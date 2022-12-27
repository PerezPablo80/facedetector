# from statistics import harmonic_mean
import requests
import cv2
import numpy as np
import face_recognition
import datetime as dt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

# import images:
# print(os.getenv("QUERY_IMAGES"))
pathQuery = os.getenv("QUERY_IMAGES", default='ImagesQuery')
pathDetected = os.getenv("DETECTED_IMAGES", default='ImagesDetected')
cascadeDetector = os.getenv("FACE_CASCADE_DETECTOR",
                            default="haarcascade_frontalface_default.xml")
savedImages = []
quit = False
maxBlurr=300
# Load images from path and encode facenames and face encoding


def loadImagesAndEncode(path):
    known_face_encoding = []
    known_face_names = []
    myList = os.listdir(path)
    # load images and encode names with data
    for cl in myList:
        imgCur = face_recognition.load_image_file(f'{path}/{cl}')
        # print(cl)
        img_encoding = face_recognition.face_encodings(imgCur)
        # print(img_encoding)
        if len(img_encoding) > 0:
            known_face_encoding.append(img_encoding[0])
            known_face_names.append(os.path.splitext(cl)[0])
    return known_face_encoding, known_face_names

# Check if a face is detected.


def checkDetection(frame, known_face_encoding, known_face_names):
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    if len(face_locations) > 0:
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # check for matches
            matches = face_recognition.compare_faces(
                known_face_encoding, face_encoding)
            name = "unknown"
            face_distances = face_recognition.face_distance(
                known_face_encoding, face_encoding)
            if len(matches) > 0:
                try:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    if name != 'unknown':
                        return True
                except:
                    first_match_index = -1
    return False


def bringFace(face_encoding, k_face_encoding, k_face_names=False):
    found = False
    name = "unknown"
    matches = face_recognition.compare_faces(k_face_encoding, face_encoding)
    # face_distances = face_recognition.face_distance(k_face_encoding, face_encoding)
    try:
        first_index_match = matches.index(True)
        if k_face_names != False:
            name = k_face_names[first_index_match]
            found = True
        elif first_index_match >= 0:
            found = True
    except:
        first_index_match = -1
    return found, name, face_encoding, k_face_encoding
# detect face and put name on it


def detectFace(frame, known_face_encoding, known_face_names, unknown_face_encoding):
    # resize for better performance
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # convert BGR color (from openCV) to RGB color (for face_recognition)
    rgb_small_frame = small_frame[:, :, ::-1]
    # find all faces in current frame and encode them
    face_locations = face_recognition.face_locations(rgb_small_frame)
    if len(face_locations) > 0:
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            found, name, face_encoding, known_face_encoding = bringFace(
                face_encoding, known_face_encoding, known_face_names)
            if not found:
                found, name, face_encoding, unknown_face_encoding = bringFace(
                    face_encoding, unknown_face_encoding)
                if not found:
                    img = saveUnknownImage(frame)
                    imgCur = face_recognition.load_image_file(img)
                    img_encoding = face_recognition.face_encodings(imgCur)
                    if len(img_encoding) > 0:
                        unknown_face_encoding.append(img_encoding[0])
            face_names.append(name)
            # Not really necesary here, maybe but not necesary.
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                bottom *= 4
                left *= 4
                right *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255))
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left+6, bottom-6),
                            font, 1.0, (255, 255, 255), 1)
    cv2.imshow("Video", frame)
    return known_face_encoding, known_face_names, unknown_face_encoding

# send image to a server


def sendImage(filename):
    # send file
    serverURL = os.getenv("SERVER_URL", default='http://localhost:2999/')
    partial = "file"
    url = serverURL+partial
    file = pathQuery+'/'+filename
    try:
        with open(file, 'rb') as f:
            r = requests.post(url=url, files={'file': f})
    except Exception as e:
        print("send image exception")
        print(e)


# Save image on queryPath
def saveUnknownImage(frame):
    ext = '.png'
    now = dt.datetime.now()
    aux = "aa_"+now.strftime("%Y%m%d%H%M%S")
    cv2.imwrite(f'{pathQuery}/{aux}{ext}', frame)
    return pathQuery+"/"+aux+ext
# Save image on queryPath


def saveImage(frame, known_faces, known_names):
    ext = '.png'
    now = dt.datetime.now()
    aux = "aa_"+now.strftime("%Y%m%d%H%M%S")
    if not checkDetection(frame, known_faces, known_names):
        print("Guardo imagen")
        cv2.imwrite(f'{pathQuery}/{aux}{ext}', frame)
        sendImage(aux+ext)


def assignName(frame, known_faces, known_names):
    rgb_small_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    if len(face_locations) > 0:
        top *= 4
        bottom *= 4
        left *= 4
        right *= 4
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.imshow('Video', frame)


def assignNewName(fl, frame, known_faces, known_names):
    for (top, right, bottom, left) in fl:
        top *= 4
        bottom *= 4
        left *= 4
        right *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.imshow('Video', frame)

# check if image is not blurry, if value greater than 370 blurr is small

# On windows webcam max blurr is 70, on the Genius, Maxblurr is abobe 430
def blurryDetection(frame):
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(grey, cv2.CV_64F).var()
    #print("LAP:",lap)
    # maxBlurr= int(os.getenv("BLURR_MAX", default=300))
    if float(lap) > maxBlurr:
        print("Lap: ", lap)
        return True
    return False
# everyAmount is the amount of frames to skip
# delta is the time in minutes to reload known_faces and names
# path is the path where the images with known faces are


def videoCapture(everyAmount, video_capture, delta, knownPath, unknownPath):
    process_frame = 0
    delta = datetime.now() + timedelta(minutes=int(delta))
    known_face_encoding, known_face_names = loadImagesAndEncode(knownPath)
    unknown_face_encoding, unknown_face_names = loadImagesAndEncode(
        unknownPath)
    while True:
        ret, frame = video_capture.read()
        clearFrame = frame
        process_frame += 1
        if process_frame > everyAmount:
            blurr = blurryDetection(frame)
            if not blurr:
                process_frame = 0
                known_face_encoding, known_face_names, unknown_face_encoding = detectFace(
                    frame, known_face_encoding, known_face_names, unknown_face_encoding)
        if datetime.now() > delta:
            # proceso las caras de nuevo.
            known_face_encoding, known_face_names = loadImagesAndEncode(
                knownPath)
            unknown_face_encoding, unknown_face_names = loadImagesAndEncode(
                unknownPath)
        key = cv2.waitKey(1) & 0xFF  # saca la tecla digitada.
        if key == ord('s'):
            saveImage(clearFrame, known_face_encoding, known_face_names)
        if key == ord('q'):
            quit()
            break
        if key == ord('x'):
            break
        if quit == True:
            quit()
            break

# Function to quit system externally


def quit():
    quit: True
    os.system('systemctl poweroff')


def init():
    camInput = int(os.getenv("CAMERA_INPUT", default=0))
    delta = int(os.getenv("DELTA__MINUTES", default=10))
    checkEveryNFrames = int(os.getenv("CHECK_EVERY_N_FRAMES", default=50))
    # start camera input
    video_capture = cv2.VideoCapture(camInput)
    # set detection for faces
    cv2.CascadeClassifier(cascadeDetector)
    # start grabbing images
    videoCapture(checkEveryNFrames, video_capture,
                 delta, pathDetected, pathQuery)
    # release camera and close everything
    video_capture.release()
    cv2.destroyAllWindows()


init()
