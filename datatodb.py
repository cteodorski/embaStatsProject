import csv
import sqlite3
import csv
from datetime import datetime
from collections import Counter
data = dict()

conn = sqlite3.connect('datadb.db')
c = conn.cursor()
c.execute('''CREATE TABLE data (date text, quantity integer, facebookPost integer, instagramPost integer, twitterPost integer)''')



with open('data/consolidated_clean.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		date = row[0]
		quantity = int(row[1])	
		datetime_object = datetime.strptime(date,'%m/%d/%Y')
		formateddate = datetime_object.strftime("%Y-%m-%d")
		poop = {formateddate: quantity}
		if formateddate in data:
			data[formateddate] += quantity
		else:
			data[formateddate] = quantity
                
	



for key, value in data.iteritems():
	sqlstatement = 'INSERT INTO data VALUES ("' + key + '",' + str(value) + ',0,0,0)'
	c.execute(sqlstatement)	

conn.commit()
conn.close()












	
		


	



	

