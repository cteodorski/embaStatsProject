import json
import datetime
from collections import Counter


facebookPosts = []

with open('facebook.json', 'r') as f:
    posts_dict = json.load(f)

for post in posts_dict['status_updates']:
	epoch = post['timestamp'] 
        date = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d')
	facebookPosts.append(date) 

post_count = Counter(facebookPosts)

for date in sorted(post_count):
	print date, post_count[date]
