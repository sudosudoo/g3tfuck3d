import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com.au', 'www.bom.gov.au/?ref=logo', 'reddit.com/r/ooer', 'youtube.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)