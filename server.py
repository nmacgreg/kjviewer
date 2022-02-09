from flask import Flask
app = Flask(__name__)

import json
from json2html import *
with open('/home/nmacgreg/.kijiji_scraper/ads.json', 'r') as myfile:
    jsondata = myfile.read()
# parse through the data, transforming data into links

cars = json.loads(jsondata)

for id, details in cars.items():
    for key, value in details.items():
        if key == "Url":
           cars[id][key] = "<a href=" + value + ">" + value + "</a>" 
        if key == "DataSource":
           cars[id][key] = "<a href=" + value + ">" + value + "</a>" 

#for counter in range(0, limit):
    #print(cars[counter])
    
    #print(cars[counter]['Url'])
    #cars[counter]['Url'] = '<a href=' + cars[counter]['Url'] + '>' + cars[counter]['Url'] + '</a>'



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/list')
def viewTable():
    #print(json2html.convert(json = infoFromJson))
    #return '<table><tr><td>this</td><td>that</td></tr></table>'
    #return json2html.convert(json = jsondata)
    return json2html.convert(json = cars, escape = 0)

if __name__ == '__main__':
    app.run()
