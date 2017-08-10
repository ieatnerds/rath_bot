from twython import Twython

from auth import (consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret
                  )

twitter = Twython(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret
                  )

message = "I am a bot. Beep Boop."
twitter.update_status(status=message)
