import tweepy
from datetime import datetime, timedelta

# set up Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# get tweets from the past 14 days
days = 14
now = datetime.now()
week_ago = now - timedelta(days=days)
tweets = tweepy.Cursor(api.user_timeline).items()
tweets_to_delete = [tweet for tweet in tweets if tweet.created_at < week_ago]

# delete old tweets
for tweet in tweets_to_delete:
    api.destroy_status(tweet.id)
    print(f'Deleted tweet with ID {tweet.id_str}')
