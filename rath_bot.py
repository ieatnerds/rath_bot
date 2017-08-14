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

logging.basicConfig(filename='logs/record.log', level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

message = check_weather.grab_temp()
twitter.update_status(status=message)
logging.info('I Tweeted!\n')
exit()
