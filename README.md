# Facedetector

**Created: Pablo Perez <perez.pablo@gmail.com>**

---

## Instalation

### For Ubuntu:

sudo apt install dirmngr apt-transport-https ca-certificates
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

sudo apt install gcc g++ cmake curl
sudo apt install python3-pip

### For Python

pip3 install flask flask-cors filehandler python-dotenv
pip3 install requests
pip3 install opencv-python
pip3 install face-recognition
pip3 install --upgrade pyside2 pyqt5

pip freeze > requirements.txt

### For rect frontend

npx create-react-app frontend
cd frontend
npm i react-router react-router-dom axios react-bootstrap bootstrap
npm i react-scripts

### Clone repository:

(on an empty folder)

git clone https://github.com/PerezPablo80/facedetector.git

### Environmental variables needed:

#### Python

DETECTED_IMAGES = folder
QUERY_IMAGES = folder
FACE_CASCADE_DETECTOR = "haarcascade_frontalface_default.xml"
CHECK_EVERY_N_FRAMES = 10
SERVER_URL = "http://localhost:2999/"
PYTHON_SERVER_PORT = 2998
REJECT_AMOUNT_OF_FRAMES = 50
CAMERA_INPUT = 0
DELTA_MINUTES = 20

## For starting on startup of ubuntu (different linux may vary):

change script to start on the folder created (in my case:home/compartida/facedetector)

Then go to start -> startup application

Create a new startup with the route of the `script.sh`

enjoy
