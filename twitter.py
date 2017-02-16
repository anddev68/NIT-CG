# -*- coding: utf-8 -*-

#import twitter
import re

#auth = twitter.OAuth(consumer_key="",
#consumer_secret="",
#token="",
#token=secret="")

PATTERN = r'.*([1-5])([MEDCAYSK]).*'
match = re.search(PATTERN, '1Yの時間割教えて')

print(match.group(1))
print(match.group(2))

#t = twitter.Twitter(auth=auth)
#Userstreamを用いる
#t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

#自分のタイムラインのツイートおよびユーザーの情報が流れる
#for msg in twitter.userstream.user():
#    if msg['text'].find(""):
        

