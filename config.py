import tweepy
import logging
import os
from dotenv import load_dotenv

# Capture errors and info messages
logger = logging.getLogger()

# Trace path of .env:
load_dotenv('.env')


# Authorize twitter API
def call_twitter_api():
    # Get the variable values
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Confirm validity of credentials
    try:
        api.verify_credentials()

    except Exception as exc:
        logger.error("Error creating API", exc_info=True)
        raise exc
    logger.info("API created")
    return api
