from twython import Twython
from tim import tim

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)



message = (tim)
twitter.update_status(status=message)
print("Tweeted: %s" % message)
