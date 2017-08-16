from scrapy import cmdline

import MySQLdb
import sys
import datetime
import time

db = MySQLdb.connect("localhost","root","123456","fairy",charset='utf8')

cursor = db.cursor()

sql2 = "truncate table fairy.t_changeList"

print sql2
cursor.execute(sql2)

cmdline.execute("scrapy crawl fairy".split())