#!/usr/bin/python

import json
from json2html import *
import os
import sqlite3
import re

conn = sqlite3.connect('data/cars.db')
print("Opened database successfully");
 
# Get the list of all files and directories
path = "data/"
dir_list = os.listdir(path)

days = []
for file in dir_list:
    if re.search(".json$", file):     # only the .json files
        with open("data/" +file, 'r') as myfile:
            jsondata = myfile.read()
        days.append(json.loads(jsondata))  # an array of dicts

# This does not keep track of differences beween the data, but maybe it combines the contents of multiple different files ?
print("Inserting data from ? days worth of data", len(days))
counter=0
errorCounter=0
for cars in days:
    for id, details in cars.items():
        # Data cleaning
        cars[id].setdefault('Title', '--No title given--') # Sometimes there is no title!
        for key, value in details.items():
            cars[id][key] = re.sub(r'\s{2,50}', '', value) # Some fields contain a ton of whitespace

        try: 
            conn.execute("INSERT INTO CARS (ID, TITLE, IMAGE, URL, DETAILS, DESCRIPTION, LOCATION, PRICE) VALUES ( ?, ? , ? , ? , ? , ? , ?, ?) ", \
            (id, details["Title"], details["Image"], details["Url"], details["Details"], details["Description"], details["Location"], details["Price"]))
            conn.commit()
            counter += 1
        
        except sqlite3.Error as error:
            print("ID:" + id + " could not be added", error)
            errorCounter += 1

print("Total # of records added: ", counter)
print("Number of errors: ", errorCounter)
conn.commit()
conn.close()
