"""
Author: importantnk@gmail.com
This script will use the Weather Underground to get the temperature of
rochester NY.

To be imported into rath_bot.py and used to return a message to be tweeted

...Powered by Weather Underground...
"""

import json
from urllib.request import urlopen
from auth import api_key

"""
This dictionary will hold unicode emojis to be added to the twitter message
based on what the weather field indicates.
"""
w_emoji = {'Clear': '\U00002600', 'Rain': '\U0001f327', 'Snow': '\U0001f328',
           'Thunder': '\U0001f329', 'Fog': '\U0001f32b', 'Cloud':'\U00002601',
           'Partly': '\U000026c5'}


# This is a list of condition to be synonymous with rain.
def sanity_weather(condition):
    """
    This function will take in the current condiition (aka weather, aka clear,
    cloudy, etc. Then it will put it into more appropriate words for status.
    It will also use the dictionary of emojis to add an emoji to the end of the
    condition, because why the hell not. I'm still a youngin'.

    After this we will return a string value to be used in the final message
    to be posted to twitter.
    """
    part_mess = 'It is: '  # This will hold onto our piece of the message
    if 'Clear' in condition:
        part_mess += 'Clear ' + str(w_emoji['Clear'])
    elif 'Thunder' in condition:
        part_mess += 'Storming ' + str(w_emoji['Thunder'])
    elif 'Rain' in condition or 'Drizzle' in condition:
        part_mess += 'Raining ' + str(w_emoji['Rain'])
    elif 'Snow' in condition:
        part_mess += 'Snowing ' + str(w_emoji['Snow'])
    elif 'Fog' in condition:
        part_mess += 'Foggy ' + str(w_emoji['Fog'])
    elif 'Partly' in condition:
        part_mess += 'Partly Cloudy ' + str(w_emoji['Partly'])
    elif 'Cloud' in condition or 'Overcast' in condition:
        part_mess += 'Cloudy ' + str(w_emoji['Cloud'])
    else:
        part_mess += str(condition) + 'y'

    return part_mess


def hot_cold(temp_f):
    """
    This function will simply add a fire or snow emoji based on the current
    temperature
    :param temp_f:
    :return:
    """
    part_mess = str(temp_f) + '°F '
    if temp_f >= 80.0:
        part_mess += '\U0001f525'
    elif temp_f <= 65.0:
        part_mess += '\U00002744'

    return part_mess


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
    temp_f = parsed_json['current_observation']['temp_f']  # Literal Temp
    weather = parsed_json['current_observation']['weather']
    condition = sanity_weather(weather)  # Condition to be used in message.
    temp = hot_cold(temp_f)  # Temp to be used in message.
    message = ("Current temperature in %s is: %s\n%s\nPowered by Weather Underground\nI am a bot, Beep Boop." % (location, temp, condition))
    return message
