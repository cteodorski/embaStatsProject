import json
import datetime
from collections import Counter
import sqlite3

conn = sqlite3.connect('datadb.db')
c = conn.cursor()

facebookPosts = []

with open('data/facebook.json', 'r') as f:
    posts_dict = json.load(f)

for post in posts_dict['status_updates']:
	epoch = post['timestamp'] 
        date = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d')
	facebookPosts.append(date) 

post_count = Counter(facebookPosts)

for date in sorted(post_count):
	sqlstatement = 'UPDATE or IGNORE data SET facebookPost=' + str(post_count[date]) + ' WHERE date="' + date + '";'
	#print sqlstatement 
        c.execute(sqlstatement)

conn.commit()
conn.close()

