import json
import os
import random
import time
import webbrowser

import requests

# Change variables according to use case
MUSIC_VIDEO = 'https://www.youtube.com/watch?v=ZPm3FSTbrQ4'
SEARCH_TERM = 'dance'
API_KEY = os.environ['TENOR_API_KEY']
GIF_LIMIT, GIF_KICKIN_TIME, GIF_CHANGE_TIME = 20, 5, 3

gifs_json = f"https://api.tenor.com/v1/search?q={SEARCH_TERM}&key={API_KEY}&limit={GIF_LIMIT}"

def get_new_gif():
    response = requests.get(gifs_json)
    content = response.content
    results = json.loads(content)['results']
    return random.choice(results)['media'][0]['gif']['url']


def run():
    webbrowser.get('firefox').open(MUSIC_VIDEO, new=1)
    time.sleep(GIF_KICKIN_TIME)

    new_gif = get_new_gif()

    while True:
        webbrowser.get('chrome').open(new_gif, new=2)
        last_gif = new_gif
        while last_gif == last_gif:
            new_gif = get_new_gif()
        time.sleep(GIF_CHANGE_TIME)


if __name__ == '__main__':
    run()
