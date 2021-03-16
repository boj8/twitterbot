import tweepy
import textmanager
import time
from datetime import datetime
from os import environ

#keys = textmanager.getTwitterKeys()

auth = tweepy.OAuthHandler(environ['CONSUMER_KEY'], environ['CONSUMER_SECRET'])
auth.set_access_token(environ['ACCESS_KEY'], environ['ACCESS_SECRET'])

api = tweepy.API(auth)
count = 0

while True:
    sentence = textmanager.getRandomSentence()
    while len(sentence) > 280:
        print('Too long:')
        print(sentence)
        sentence = textmanager.getRandomSentence()
    if count == 7:
        count = 0
        tweet = api.home_timeline()[0]
        api.update_status('@' + tweet.user.screen_name + ' ' + sentence, in_reply_to_status_id=tweet.id)
    else:
        count += 1
        api.update_status(sentence)
    
    print(count)
    print(str(datetime.now()))
    print(sentence)
    time.sleep(600)
