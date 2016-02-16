#!/usr/bin/env python
"""
Default settings template, this should be added to your python_src/settings.py file
"""

import pymysql


DATABASE = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': '',
}

# Currency API example:
# http://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2013-09-05
COINDESK_API = "http://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s"


connection = pymysql.connect(**DATABASE)
connection.close()
