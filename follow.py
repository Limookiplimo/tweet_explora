import tweepy
import logging
from config import call_twitter_api
import time

# Track logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Follow your followers
def create_follows(api):
    logger.info('Following new followers')
    for follower in tweepy.Cursor(api.get_followers).items():
        if not follower.following:
            logger.info(f'Following{follower.name}')
            follower.follow()


# Create an API object
def main():
    api = call_twitter_api()
    while True:
        create_follows(api)
        logger.info('Almost there...')
        time.sleep(45)


if __name__ == '__main__':
    main()
