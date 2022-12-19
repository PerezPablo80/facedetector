import newfacedetector as facedetector
import os
from dotenv import load_dotenv
load_dotenv()

test = os.getenv("TEST")
print(test)
facedetector.init()
