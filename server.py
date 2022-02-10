from flask import Flask
app = Flask(__name__)

import json
from json2html import *
import os
 
# Get the list of all files and directories
path = "data/"
dir_list = os.listdir(path)

days = []
for file in dir_list:
    with open("data/" +file, 'r') as myfile:
        jsondata = myfile.read()
    days.append(json.loads(jsondata))  # an array of dicts

# This does not keep track of differences beween the data, but maybe it combines the contents of multiple different files ?
for cars in days:
    for id, details in cars.items():
        for key, value in details.items():
            if key == "Url":
               cars[id][key] = "<a href=" + value + ">" + value + "</a>" 
            if key == "DataSource":
               cars[id][key] = "<a href=" + value + ">" + value + "</a>" 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/list')
def viewTable():
    return json2html.convert(json = cars, escape = 0)

if __name__ == '__main__':
    app.run()
