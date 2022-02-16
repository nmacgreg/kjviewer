#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('data/cars.db')

print("Opened database successfully")


conn.execute('''CREATE TABLE CARS
         (ID INT PRIMARY KEY    NOT NULL,
         TITLE          TEXT    NOT NULL,
         IMAGE          TEXT    NOT NULL,
         URL            TEXT    NOT NULL,
         DETAILS        TEXT    NOT NULL,
         DESCRIPTION    TEXT    NOT NULL,
         LOCATION       TEXT    NOT NULL,
         PRICE          TEXT    NOT NULL);''')
print("Table created successfully");

conn.close()
