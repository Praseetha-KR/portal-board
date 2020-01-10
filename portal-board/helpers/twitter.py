import os
import tweepy
from dotenv import load_dotenv
from logger import logger


load_dotenv(verbose=True)


class Twitter:
    def __init__(self):
        CONSUMER_KEY = os.getenv("PB_TWITTER_CONSUMER_KEY")
        CONSUMER_SECRET = os.getenv("PB_TWITTER_CONSUMER_SECRET")
        ACCESS_TOKEN = os.getenv("PB_TWITTER_ACCESS_TOKEN")
        ACCESS_TOKEN_SECRET = os.getenv("PB_TWITTER_ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(auth)
        logger.debug('Twitter API initialized')

    def tweet(self, msg: str) -> bool:
        if not msg:
            logger.warn('Tweet failed: Empty status message')
            return False

        try:
            self.api.update_status(msg)
            logger.info(f'Tweet successful')
            return True
        except tweepy.TweepError as e:
            logger.error(f'Tweet failed: {e.reason}')

        return False
