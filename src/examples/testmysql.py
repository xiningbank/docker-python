#!/usr/bin/python3

import pymysql

# Database configuration
db_host = ''
db_port = 3306
db_user = ''
db_password = ''
db_database = ''

# Open database connection
conn = pymysql.connect(host = db_host, port = db_port, user = db_user, passwd = db_password, db = db_database)

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# execute SQL query using execute() method.
cursor.execute('SELECT VERSION()')

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ('Database version : %s' %(data))

# disconnect from server
conn.close()

