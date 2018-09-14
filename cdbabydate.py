import csv
from datetime import datetime
from collections import Counter
data = dict()

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

print data

 













	
		


	



	

