import tweepy
import time

auth = tweepy.OAuthHandler('GUpeqQ2qUMyz3tdgnKyEh75Wg',
                           '39ummHYwOyVzOSDAJesI9lATUmr4Z3em1xBSW032izHkvGMWGz')
auth.set_access_token('1037961976037560321-2DhZCgYxNI1WAAgxxDjN1WuWwgNX5P',
                      '7J8WWQTdEVP6axmmSjkUGyCHILuveEZJIwiOxWOP3zLJn')

api = tweepy.API(auth)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_term = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_term).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'somename':
#         follower.follow()
#         break

# print(api.me())

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
