#!/usr/bin/python
import requests
import json
from movie import movie

class Apple(object):
    """
    Apple iTunes API
    """

    def __init__ (self):
        self.base_url = 'https://itunes.apple.com/search?'

    def get_movie_by_title(self, title, filter=None):
        '''
        '''
        country = 'US'
        media = 'movie'
        entity = 'movie'
        limit = 1

        payload = {'term': title,
                   'country': country,
                   'media': media,
                   'entity': entity,
                   'limit': limit
                  }
        r = requests.get(self.base_url, params=payload)
        results = json.loads(r.text.strip())
        results = results.get('results')[0]
        m = {}

        if results.get('trackName') == title:
            m = movie(str(results.get('trackName')), 'iTunes')
            m.stream = True
            m.price_stream = results.get('trackPrice')

        return m
