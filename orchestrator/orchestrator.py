from flask import Flask
from flask import request
from waitress import serve
from model import is_suspicious
import os
import logging
import random
import json
import requests


os.environ['PORT'] = '8081'
# os.environ['PORT'] = '1234'

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)



@app.route("/start",methods=['POST'])
def run():
    print(request.data)
    encoding = 'utf-8'
    data_str = request.data.decode(encoding) 
    data_str = data_str.replace("\'", "\"")


    sku = json.loads(data_str)['sku']
    print(f"Sku - {sku}")
    res = requests.get(f'http://0.0.0.0:1234/demo?msg={sku}')
    
    # Do something ---- 
    # requests.post('http://0.0.0.0:1234/model', data_str)

    return 0


@app.route("/model",methods=['POST'])
def model():
    # print(type(request))
    # print(request.get_json())
    print(request.data)
    print(type(request.data))
    encoding = 'utf-8'
    data_str = request.data.decode(encoding) 
    data_str = data_str.replace("\'", "\"")
    print(data_str)
    print(type(data_str))

    model_output = is_suspicious(data_str)
    print(model_output)
    return model_output
  

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8081)))