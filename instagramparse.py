import json
import datetime
from collections import Counter


instagramPosts = []

with open('data/instagram.json', 'r') as f:
    posts_dict = json.load(f)

for post in posts_dict['photos']:
	splitdate = post['taken_at'].split('T') 
        date = splitdate[0]
	instagramPosts.append(date) 

post_count = Counter(instagramPosts)

for date in sorted(post_count):
	print date, post_count[date]
