import os
import threading
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
import facedetector
import file_handler
load_dotenv()
# test= os.getenv("TEST")

app = Flask(__name__)
previousFolder = os.getenv("QUERY_IMAGES")
actualFolder = os.getenv("DETECTED_IMAGES")


@app.route('/status', methods=['GET'])
def init():
    return {"Status": "true", "message": " all ok"}


@app.route('/file', methods=['PUT', 'GET'])
def actions():
    if request.method == 'GET':
        return file_handler.listFiles(actualFolder)
    elif request.method == 'PUT':
        previousFile = previousFolder+"/"+request.json['previousName']
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


def fcinit():
    facedetector.init()


def serverStart():
    app.run(port=2999)
    # app.run(host='0.0.0.0',port=4434)
    # app.run()


t1 = threading.Thread(target=fcinit)
t2 = threading.Thread(target=serverStart)
t1.start()
t2.start()
