import tweepy
import time
import random
import os
from hashtags import hashtag
from tweets import tweet




# Authenticate to Twitter
auth = tweepy.OAuthHandler("ConYb1zQ7WhBEYPfxVsi1zt0w",
                           "g4ujAFUq0TZtSDogGfj7p1i4kxmSPoTvL6BYGfHLclFRWRVhnh")
auth.set_access_token("956507305960509440-WyKQ83Kac4w4WOqiZQylndVgwAD1wc2",
                      "6gi3toMbAyYTMDWkmdaGjr93n5nlwKvhfhkDmFYvPv09t")


api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


api.update_status(random.choice(hashtag) + random.choice(tweet))

time.sleep(184)

api.update_status(random.choice(hashtag) + random.choice(tweet))

time.sleep(269)

api.update_status(random.choice(hashtag) + random.choice(tweet))
