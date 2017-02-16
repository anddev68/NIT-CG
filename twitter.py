# -*- coding: utf-8 -*-

#import twitter
import re

auth = twitter.OAuth(consumer_key="",
consumer_secret="",
token="",
token=secret="")

PATTERN = r'.*([1-5])([MEDCAYSK]).*'
TWITTER_ID = ""

t = twitter.Twitter(auth=auth)
t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

for msg in twitter.userstream.user():
    # リプライに反応
    if msg['in_reply_to_screen_name']==TWITTER_ID:
        # マッチした場合のみ反応
        if re.match(PATTERN, msg['text']):
            match = re.search(PATTERN, msg['text'])
            print(match.group(1))
            print(match.group(2))
            tweet = "@"+ msg['user']['screen_name']
            t.statuses.update(status=tweet)
        else:
            print("構文が間違っています")


