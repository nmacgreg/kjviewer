from flask import Flask
app = Flask(__name__)

import json
from json2html import *
import os
import sqlite3


#conn.execute('''CREATE TABLE CARS
         #(ID INT PRIMARY KEY    NOT NULL,
         #TITLE          TEXT    NOT NULL,
         #IMAGE          TEXT    NOT NULL,
         #URL            TEXT    NOT NULL,
         #DETAILS        TEXT    NOT NULL,
         #DESCRIPTION    TEXT    NOT NULL,
         #LOCATION       TEXT    NOT NULL,
         #PRICE          TEXT    NOT NULL);''')
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/list')
def viewTable():
    conn = sqlite3.connect('data/cars.db')
    cur = conn.cursor()
    cur.execute("SELECT price, substring(title, 1, 30), substring(details, 1, 20), URL FROM cars order by price")
    bigarray =[]
    for row in cur:
        #print(row)
        newdict={"Price":row[0], "Title":row[1], "Details":row[2], "URL":"<a href=\"" + row[3] +"\">" + row[3] + "</a>"}
        bigarray.append(newdict)
    conn.close()
    # convert dict to json 
    cars = json.dumps(bigarray,indent=4)
    return json2html.convert(json = cars, escape = 0)

if __name__ == '__main__':
    app.run()
