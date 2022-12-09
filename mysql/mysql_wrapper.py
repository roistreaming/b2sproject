import mysql.connector
from flask import Flask
from flask import request
from sqlenrich import sql_enrich,sql_connect

from waitress import serve
import os
import logging
import random
import json


app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)
cnx = sql_connect('10.26.194.22','b2s','b2suser','ROI2022cb')




@app.route("/demo",methods=['GET'])
def demoget():
  returnstring = 'demo - GET received'
  s_msg = str(request.args.get('msg'))
  returnstring = sql_enrich(s_msg, cnx)
  return returnstring



@app.route("/demo",methods=['POST'])
def demopost():
  returnstring = "demo - POST received\n"
  s_msg = str(request.args.get('msg'))
  returnstring = sql_enrich(s_msg, cnx)
  return returnstring



if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 1234)))