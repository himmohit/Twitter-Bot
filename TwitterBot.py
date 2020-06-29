import tweepy
import time

auth = tweepy.OAuthHandler('VEV6FAvoRhxZp05IO7gnxmHP4','l3Ue38Ivm9tOdTUpmeQMbsHzYBsMlP9jyOpVyzLRAQmwzRBh1s')
auth.set_access_token('1450490106-BVgLqA9bQvC2boSvKOpKEYzp9Ps8eXJ6AsEBvJd','U5ztXxY0GoiVzneXF3ZXyuWj6q9kEjvvS1dRbJpAjL3yo')

api = tweepy.API(auth, wait_on_rate_limit="True", wait_on_rate_limit_notify=True)

user = api.me()

search = 'sachin_tendulkar'
nrTweets = 20

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
