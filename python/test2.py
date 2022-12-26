
import cv2
import numpy as np
import face_recognition
import os
from dotenv import load_dotenv
load_dotenv()

test = os.getenv("TEST")
print(test)
print(cv2.__version__)
