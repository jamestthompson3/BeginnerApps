import tweepy
from tweepy import Stream
from tweepy import StreamListener
ckey='FpBa0sYmFQM9XaT2nggWLtXWo'
consumer_secret='l3iUlawJcdtbvQx4c1gOk1vp3Dph0u5VuDiy54LWyA0OtoHdJ4'
access_token='2242519351-iwZ3jBVxme0a7Czo9OT9LsHXKvJcl9QZtUoU8kZ'
access_token_secret='fzBFJveF6YB8Pa7nava6sBXiIdkwvQOFxSdSD49OdqNSh'
auth= tweepy.OAuthHandler(ckey,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
#class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])
 
        return true
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 
#if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(ckey, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 
    stream = Stream(auth, listener)
    stream.filter(track=['#Trump'])
print(API.trends_location(1))