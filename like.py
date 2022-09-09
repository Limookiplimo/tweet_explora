import tweepy
import logging
from config import call_twitter_api

# Track logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class liketweet(tweepy.Stream):

    def __init__(self, api):
        self.api = api
        self.me = api.get_user()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        # Check if am the tweet author or it is a reply
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            # Like the tweet
            try:
                tweet.favorite()
            except Exception as exc:
                logger.error("Error on liking", exc_info=True)
                raise exc

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = call_twitter_api()
    tweets_listener = liketweet(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    main(["Python", "Data Analysis"])
