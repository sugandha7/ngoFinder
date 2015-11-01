#!/usr/bin/python

import MySQLdb
import config
db = MySQLdb.connect(host="localhost",user=config.username,passwd=config.password)
db1 = db.cursor()
db1.execute('DROP DATABASE IF EXISTS ngo')
db1.execute('CREATE DATABASE ngo')
db.commit()
db.close()
db = MySQLdb.connect("localhost",config.username, config.password, "ngo" )
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS \
ngo (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
 name VARCHAR(50),\
 address VARCHAR(255),\
 latitude FLOAT,\
 longitude FLOAT,\
 website VARCHAR(50),\
phone VARCHAR(20),\
mobile VARCHAR(20),\
email VARCHAR(255),\
purpose VARCHAR(255),\
aim VARCHAR(500),\
person VARCHAR(50))')
db.commit()
db.close()