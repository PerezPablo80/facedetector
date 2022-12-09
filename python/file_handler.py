import os
from dotenv import load_dotenv
load_dotenv()


def emptyFolder(folder):
    try:
        myList = os.listdir(folder)
        # load images and encode names with data
        for fl in myList:
            os.unlink(folder+'/'+fl)
        return {"status": "true", "message": "Folder empty"}
    except Exception as e:
        return {"status": "false", "message": "exception found", "error": e}


def listFiles(folder):
    try:
        lista = []
        myList = os.listdir(folder)
        # load images and encode names with data
        for fl in myList:
            lista.append(fl)
        return {"status": "true", "lista": lista}
    except Exception as e:
        return {"status": "false", "message": "exception found", "error": e}


def update(previousName, actualName):
    try:
        if (os.path.isfile(previousName) and not os.path.isfile(actualName)):
            os.rename(previousName, actualName)
        else:
            return {"status": "false", "message": "actualizacion incorrecta, archivo a actualizar inexistente o nombre nuevo existente"}
        return {"status": "true", "message": "actualizacion correcta"}
    except Exception as e:
        return {"status": "false", "message": "exception found", "error": e}
