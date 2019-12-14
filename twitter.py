import tweepy
import constants

class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key=constants.consumer_key, consumer_secret=constants.consumer_secret)
        self.auth.set_access_token(constants.access_key, constants.access_secret)
        self.api = tweepy.API(self.auth)


    def post_tweet_with_media(self):
        try:
            self.api.update_with_media("ready.png")
            print("Tweeted!")
        except Exception as e:
            print(str(e))
            pass