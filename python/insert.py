import os
from mysql import connector
import csv

cnx = connector.connect(host='localhost', user='ai', passwd='zhang', db='bodypart')

cursor = cnx.cursor()

query = "insert into heart_shadow(FILENAME, ID) VALUE (%s, %s)"

with open('heart_shadow.csv', 'r') as f:
    reader = csv.reader(f)
    cnt = 0
    for row in reader:
        filename =  row[0]
        Id = cnt
        cnt += 1
        cursor.execute(query, (filename, Id))
        if cnt % 100 == 0:
            cnx.commit()
            print cnt

cnx.commit()
cursor.close()
cnx.close()
