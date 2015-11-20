#!/usr/bin/python

import MySQLdb
import secret_settings
db = MySQLdb.connect(host="localhost",user=secret_settings.user,passwd=secret_settings.password)
db1 = db.cursor()
db1.execute('DROP DATABASE IF EXISTS ngo')
db1.execute('CREATE DATABASE ngo')
db.commit()
db.close()
