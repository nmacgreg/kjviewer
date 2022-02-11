#!/usr/bin/python

import json
from json2html import *
import os
import sqlite3

conn = sqlite3.connect('cars.db')
print("Opened database successfully");

 
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
        print("Found id=" + id + " where Title is: " + details["Title"])    
        try: 
            conn.execute("INSERT INTO CARS (ID, TITLE, IMAGE, URL, DETAILS, DESCRIPTION, LOCATION, PRICE) \
            VALUES (" + id + ", " + details["Title"] + ", " + details["Image"] + ", " +  details["Url"] + ", " + details["Details"] + ", " + details["Description"] + ", " + details["Location"] + ", " +  details["Price"] + ")")
        
        except sqlite3.Error as error:
            print("ID:" + id + " could not be added", error)

        #for key, value in details.items():
            #if key == "Url":
               #cars[id][key] = "<a href=" + value + ">" + value + "</a>" 
            #if key == "DataSource":
               #cars[id][key] = "<a href=" + value + ">" + value + "</a>" 

conn.close()
