"""
This script will hopefully check and return cpu usage in an easily read format.
This will be used to report to my twitter bot so I can have it post when CPU
usage is high. This is practice for automation and stuff I guess.
"""

import time
import psutil
while True:
    percent = psutil.cpu_percent(interval=1)
    if percent >= 10.0:
        print(percent)
    time.sleep(2)
