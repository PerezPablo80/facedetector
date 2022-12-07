import os
from dotenv import load_dotenv
from flask import Flask
load_dotenv()
# test= os.getenv("TEST")

app = Flask(__name__)


@app.route('/', methods=['GET'])
def init():
    return 'Hello world'


app.run()
