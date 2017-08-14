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
from make_dir import make_dir
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

if len(sys.argv) == 1:
    path = 'logs/'  # Default for testing
else:
    path = str(sys.argv[1])  # To actually be used on the rpi

make_dir(path)

logging.basicConfig(filename=(path+'record.log'), level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

message = check_weather.grab_temp()

try:
    twitter.update_status(status=message)
    logging.info('I Tweeted!\n')
except Exception as err:
    logging.info(str(err)+'\n')  # Actually helpful
exit()
