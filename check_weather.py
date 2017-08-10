"""
This script will use the OpenWeatherMap to get the temperature of
rochester NY. or at the very least that rochester is the one being given to me.
Being that there are multiple Rochesters in the United States I'm unsure
how I can differentiate that at the current time. Not that it's super important
to me, since Rochester, NY is the city I wanted anyways.
"""

import pyowm
from auth import owm_key

owm = pyowm.OWM(owm_key)

observation = owm.weather_at_place('Rochester, US')

w = observation.get_weather()
weather_dict = w.get_temperature('fahrenheit')
temp = weather_dict['temp']
print(temp)
