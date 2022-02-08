from flask import Flask
app = Flask(__name__)

import json
from json2html import *
with open('/home/nmacgreg/.kijiji_scraper/ads.json', 'r') as myfile:
    jsondata = myfile.read()

# transform that into a local datastructure
vlans = json.loads(jsondata)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/list')
def viewTable():
    #print(json2html.convert(json = infoFromJson))
    #return '<table><tr><td>this</td><td>that</td></tr></table>'
    return json2html.convert(json = jsondata)

if __name__ == '__main__':
    app.run()
