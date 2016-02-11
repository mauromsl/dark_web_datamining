#!/usr/bin/env python
''' D``efault settings template, this should be added to your python_src/settings.py file '''

import mysql.connector
from mysql.connector import errorcode


DATABASE={
	'user':'root',
	'password':'',
	'host':'127.0.0.1',
	'database':'', 
}


try:
  connection = connector.connect(**DATABASE)
except connector.Error as error:
  if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif error.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(error)
else:
  connection.close()