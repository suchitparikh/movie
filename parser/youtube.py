#!/usr/bin/python

import cgi
import gdata.service
import gdata.youtube
import gdata.youtube.service

import ConfigParser
import json
from httplib import HTTPConnection
import urllib

from movie import movie

class Youtube(object):
    """
    Youtube API parser
    """

    def __init__(self):

        section = "youtube"
        config = ConfigParser.SafeConfigParser()
        config.readfp(open('../config.cfg'))

        DEVELOPER_KEY = config.get(section, 'DEVELOPER_KEY_V2')
        YOUTUBE_API_SERVICE_NAME = config.get(section, 'YOUTUBE_API_SERVICE_NAME')
        YOUTUBE_API_VERSION = config.get(section, 'YOUTUBE_API_VERSION')

    def get_movie_by_title(self, title):
        '''
        Args:
            title - Title of the movie
        '''

        search_term = cgi.escape(title)
        client = gdata.youtube.service.YouTubeService()
        query = gdata.youtube.service.YouTubeVideoQuery()
        query.prettyprint = True
        query.key=DEVELOPER_KEY
        query.v = YOUTUBE_API_VERSION
        query.vq = search_term
        query.max_results = '2'
        feed = client.YouTubeQuery(query)

        m = movie('', 'Youtube')

        for entry in feed.entry:
            m.movie = entry.title.text
            m.stream = 'True'
            m.price_stream = 0
            break

        return m

if __name__ == '__main__':
    y = Youtube()
    y.get_movie_by_title('Argo')
