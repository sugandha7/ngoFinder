#!/usr/bin/python

import MySQLdb
import config
db = MySQLdb.connect(host="localhost",user=config.username,passwd=config.password)
db1 = db.cursor()
db1.execute('DROP DATABASE IF EXISTS ngo')
db1.execute('CREATE DATABASE ngo')
db.commit()
db.close()
