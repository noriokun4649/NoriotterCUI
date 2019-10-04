# -*- encoding: utf-8 -*-
import twitter  # pip install python-twitter
import threading
import sys

args = sys.argv
api = twitter.Api(consumer_key=args[1],  # コマンドライン実行時にパラメータとして渡してね
                  consumer_secret=args[2],  # コマンドライン実行時にパラメータとして渡してね
                  access_token_key=args[3],  # コマンドライン実行時にパラメータとして渡してね
                  access_token_secret=args[4])  # コマンドライン実行時にパラメータとして渡してね


def input_get():
    while True:
        stings = input()
        if not stings:
            print("文字がないな。ツイートできないぞ")
        else:
            api.PostUpdate(status=stings)
            print("Tweetしたぞ:" + stings)


th = threading.Thread(target=input_get)
th.start()
followeid = api.GetFriendIDs(cursor=-1)
followidstr = map(str, followeid)
print("Count:" + str(len(followeid)))
stream = api.GetStreamFilter(follow=followidstr)
for tweet in stream:
    # print(tweet)
    if 'text' in tweet:
        if tweet['in_reply_to_user_id'] in followeid or not tweet['in_reply_to_user_id']:
            userdata = tweet['user']
            if userdata['id'] in followeid:
                print('-------------------------------')
                print(userdata['name'] + " @" + userdata['screen_name'])
                print(tweet['text'])
                print(tweet['source'])
