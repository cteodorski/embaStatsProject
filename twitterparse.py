import pandas
from datetime import datetime
from collections import Counter
twitterPosts = []

fieldnames = ['favorite_count','source,text','in_reply_to_screen_name','is_retweet','created_at','retweet_count','id_str']
csvfile = pandas.read_csv('data/twitter.csv', names=fieldnames)
dates = csvfile.created_at.tolist()
for date in dates:
	date = date.replace(" +0000","")
	datetime_object = datetime.strptime(date,'%a %b %d %H:%M:%S %Y')
 	formateddate = datetime_object.strftime("%Y-%m-%d")
	twitterPosts.append(formateddate)
	
post_count = Counter(twitterPosts)

for date in sorted(post_count):
	print date, post_count[date]

