import tweepy
import keys
import time
import pdb #I used this to debug this script

print('This is my twitter bot')

auth = tweepy.OAuth1UserHandler(
   keys.consumer_key, keys.consumer_secret, keys.access_token, keys.access_token_secret
)

api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
 
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(since_id = last_seen_id,tweet_mode='extended')

  
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id

        store_last_seen_id(last_seen_id, FILE_NAME)

        if '#python3' in mention.full_text.lower():
            print('found #python3', flush=True)
            print('responding back...', flush=True)

            '''api.update_status('@' + mention.user.screen_name + '#Keep learning Python3!', mention.id)'''
            # convert docstring back to original for posting replies to mentioned hashtag 
                

'''while True:
    reply_to_tweets()
    time.sleep(15)'''
#function will run every 15 seconds later, you can reduce the time...



