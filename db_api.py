#!/usr/bin/python

import MySQLdb
import config
# Open database connection
db = MySQLdb.connect("localhost",config.username, config.password, "ngo" ) #'ngo' is the name of the database.

class writeDB(object):
    def __init__(self, idno, name, address, latitude, longitude, website, contact):
        self.id = idno
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.contact = contact
        self.website = website

			

    def insert_query(self):
		# prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Prepare SQL query to INSERT a record into the database
        sql = "INSERT INTO ngo(id, name, \
       	address, latitude, longitude, website, contact) \
        VALUES ('%d', '%s', '%s', '%f', '%f', '%s', '%s' )" % \
       (self.id, self.name, self.address, self.latitude, self.longitude \
       , self.website, self.contact)
        print sql
        try:
   		# Execute the SQL command
            cursor.execute(sql)
   			# Commit your changes in the database
            db.commit()
        except:
   			# Rollback in case there is any error
   	        db.rollback()

row = writeDB(7, "abcd","E-608, Shakurpur New Delhi Pin: 110034 Delhi", 28.6846245, 77.1338497, \
	"http://delhi.ngosindia.com/a-ideal-childrens-care-org-new-delhi/","9717817747") #sample row to be inserted into the database.

row.insert_query()

db.close()
