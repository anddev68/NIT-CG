# -*- coding: utf-8 -*-

# これは使えなさそう → http://qiita.com/yuki_bg/items/96a1608aa3f3225386b6
# こっちで→ http://qiita.com/yubais/items/dd143fe608ccad8e9f85
# http://qiita.com/nasa9084/items/40f223b5b44f13ef2925
# http://www.utali.io/entry/2016/10/06/012951

from requests_oauthlib import OAuth1
import re
import requests
import json
import conf
import core

PATTERN = r'.*([1-5])([MEDCAYSK]).*'

# REST tweet
def tweet(text, auth):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status": text}
    r = requests.post(url, auth=auth, data=params)

# Make reply message
def make_message(username, text):
    if re.match(PATTERN, text):
        # reschedule list file parse
        # then get reschedule list
        match = re.search(PATTERN, text)
        data = core.parse()
        data = list(core.filter1(match.group(1), match.group(2), data))
        if len(data) == 0:
            return "@"+ username + " 直近の授業変更はありません:" + text
        else:
            tmp = core.dumps(data)
            if len(tmp) > 100: tmp =  tmp[0:100]
            return "@"+ username + " " + tmp
    else:
        return "@"+ username + " 構文が間違っています:" + text


# Oauth Authentication
auth = OAuth1(conf.consumer_key, conf.consumer_secret, conf.token, conf.token_secret)

# Search Tweet With Streaming API
# @NITGCRescheBot's id = 832022437294247936
# [https://syncer.jp/twitter-screenname-userid-converter]
url = "https://userstream.twitter.com/1.1/user.json"
r = requests.post(url, auth=auth, stream=True, data={})
for line in r.iter_lines():
    line = line.decode('utf-8')
    if line == "":
        continue
    d = json.loads(line)
    
    # Remove my tweet
    if 'user' in d and d['user']['id_str'] == '832022437294247936':
        continue
    # Remove empty line
    if 'text' in d:
        print("Recieve:", d['text'], d['user']['id_str'])
    if 'user' in d:
        if d['user']['screen_name'] is not None:
            # reply to user
            msg = make_message(d['user']['screen_name'], d['text'])
            tweet(msg, auth)
            print("Send:", msg)
    
    #for key, value in d.items():
    #    print(key, value)
    #if d.has_key("in_reply_to_screen_name"):
    #    tweet(d['in_reply_to_screen_name'], auth)
