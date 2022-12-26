import os
import threading
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, send_file
# import newfacedetector as facedetector
from flask_cors import CORS
import file_handler
load_dotenv('/home/pachi/Desktop/facedetector/python/.env')
# test= os.getenv("TEST")

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
previousFolder = os.getenv("QUERY_IMAGES")
actualFolder = os.getenv("DETECTED_IMAGES")


@app.route('/shutdown', methods=['GET'])
def quit():
    quit: True
    os.system('systemctl poweroff')
    return {"Status": "true", "message": "Powering off"}

@app.route('/status', methods=['GET'])
def init():
    return {"Status": "true", "message": " all ok"}


@app.route('/static/<name>', methods=['GET'])
@app.route('/static/', methods=['GET'])
@app.route('/static', methods=['GET'])
def fileAccess(name=""):
    if len(name) > 0:
        if name.startswith("aa_"):
            filename = previousFolder+"/"+name
        else:
            filename = actualFolder+"/"+name
        if os.path.isfile(filename):
            return send_file(filename)
        return "<h1>No file found</h1>"
    else:
        return "<h1>NO FILE REQUESTED</h1>"


def fileExist(file):
    return os.path.isfile(file)


@app.route('/file/<folder>', methods=['PUT', 'GET', 'POST'])
@app.route('/file/', methods=['PUT', 'GET', 'POST'])
@app.route('/file', methods=['PUT', 'GET', 'POST'])
def actions(folder=""):
    if request.method == 'GET':
        fileType = folder
        if fileType == "Desconocidos":
            return file_handler.listFiles(previousFolder)
        else:
            return file_handler.listFiles(actualFolder)
    elif request.method == 'POST':
        name = request.json['fileName']
        return file_handler.delete(name, previousFolder, actualFolder)
    elif request.method == 'PUT':
        previousFile = previousFolder+"/"+request.json['previousName']
        actualFile = actualFolder+"/"+request.json['actualName']
        if (fileExist(previousFile) and not fileExist(actualFile)):
            return file_handler.update(previousFile, actualFile)
        else:
            previousFile = actualFolder+"/"+request.json['previousName']
            actualFile = actualFolder+"/"+request.json['actualName']
            return file_handler.update(previousFile, actualFile)


@app.route('/emptyFolder', methods=['PUT', 'GET'])
def folder():
    return file_handler.emptyFolder()

# app.run()

# def putter():
#     try:
#         previousName = previousFolder+"/"+request.json['previousName']
#         actualName = actualFolder+"/"+request.json['actualName']
#         if (os.path.isfile(previousName) and not os.path.isfile(actualName)):
#             os.rename(previousName, actualName)
#         else:
#             return {"status": "false", "message": "actualizacion incorrecta, archivo a actualizar inexistente o nombre nuevo existente"}
#         return {"status": "true", "message": "actualizacion correcta"}
#     except Exception as e:
#         print(e)
#         return {"status": "false", "message": "actualizacion incorrecta"}


# def facedetector_init():
#     facedetector.init()


# def serverStart():
#     app.run(host="0.0.0.0", port=2999)

# quitar esto y descomentar las dos funciones para un solo script
app.run(host="0.0.0.0", port=2999)

# t1 = threading.Thread(target=serverStart)
# t2 = threading.Thread(target=facedetector_init)
# t1.start()
# t2.start()
