"""
Author: importantnk@gmail.com
Rath Twitter Bot

This is a simple bot for twitter that is being used for several functions.
The main function of the bot is to provide an easy learning experience with
the Twitter API and pulling information from other sources to post on twitter.
"""
# Imports
import pyowm
import time
from twython import Twython
from auth import (consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret,
                  owm_key
                  )
# Setup
twitter = Twython(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret
                  )

owm = pyowm.OWM(owm_key)


# Functions

def get_temp(location, degree):
    """
    This function will use the OpenWeatherMap to find the temperature
    of a given location in a given unit.

    It will then return a float that represents the temperature.
    """
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    weather_dict = w.get_temperature(degree)
    temp = weather_dict['temp']
    return temp


while True:
    temp = get_temp('Rochester, US', 'fahrenheit')
    pre = 'The current Temp in Rochester, NY is: '
    post = '° F'
    credit = '\nThis information is from OpenWeatherMap.'
    message = (pre + str(temp) + post + credit)
    twitter.update_status(status=message)
    time.sleep(60 * 5)  # Seconds * Minutes

