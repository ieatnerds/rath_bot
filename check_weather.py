"""
This script will use the Weather Underground to get the temperature of
rochester NY.

To be imported into rath_bot.py and used to return a message to be tweeted

...Powered by Weather Underground...
"""

import json
from urllib.request import urlopen
from auth import api_key


def grab_temp():
    """
    This function will grab the temp of rochester ny in fahrenheit and
    return a message to be tweeted to the main module rath_bot.py
    :return:
    """
    html = urlopen('http://api.wunderground.com/api/'+api_key+'/geolookup/conditions/q/NY/Rochester.json')
    json_string = html.read().decode('utf-8')

    parsed_json = json.loads(json_string)

    location = parsed_json['location']['city']

    temp_f = parsed_json['current_observation']['temp_f']

    message = ("Current temperature in %s is: %s°F  \nPowered by Weather Underground\nI am a bot, Beep Boop." % (location, temp_f))
    return message
