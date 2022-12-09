from flask import Flask
from flask import request
from waitress import serve
from ..model.model import is_suspicious
import os
import logging
import random

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)


@app.route("/model",methods=['POST'])
def model():
    
    model_output = is_suspicious(request.json())
    return model_output

@app.route("/version")
def version():
  return "ROIGCP Demo 1.0\n"

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))