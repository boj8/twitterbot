import tweepy
import textmanager
import time
from datetime import datetime

keys = textmanager.getTwitterKeys()

auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])

api = tweepy.API(auth)
count = 0

while True:
    sentence = textmanager.getRandomSentence()
    while len(sentence) > 280:
        print('Too long:')
        print(sentence)
        sentence = textmanager.getRandomSentence()
    if count == 5:
        count = 0
        tweet = api.home_timeline()[0]
        api.update_status('@' + tweet.user.screen_name + ' ' + sentence, in_reply_to_status_id=tweet.id)
    else:
        count += 1
        api.update_status(sentence)
    
    print(count)
    print(str(datetime.now()))
    print(sentence)
    time.sleep(1800)