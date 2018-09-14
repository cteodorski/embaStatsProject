import csv
from datetime import datetime
from collections import Counter

with open('consolidated_clean.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		date = row[0]	
		datetime_object = datetime.strptime(date,'%m/%d/%Y')
		formateddate = datetime_object.strftime("%Y-%m-%d")
		print formateddate + ","+  row[1]
	
		


	



	

