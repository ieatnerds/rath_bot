"""
Author: importantnk@gmail.com
Rath Twitter Bot

This is a simple bot for twitter that is being used for several functions.
The main function of the bot is to provide an easy learning experience with
the Twitter API and pulling information from other sources to post on twitter.
"""
# Imports
import check_weather
import logging
import sys
from make_dir import makeDir
from twython import Twython
from auth import (consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret,
                  )

twitter = Twython(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret
                  )

# Checking if there's an argument for where to log.
if len(sys.argv) == 1:
    path = 'logs/'
else:
    path = str(sys.argv[1])

makeDir(path)

logging.basicConfig(filename=(path+'record.log'), level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

message = check_weather.grabTemp()

try:
    twitter.update_status(status=message)
    logging.info('I Tweeted!\n')
except Exception as err:
    # This is mostly to just catch 405 forbidden's on duplicates.
    logging.info(str(err)+'\n')

exit()
