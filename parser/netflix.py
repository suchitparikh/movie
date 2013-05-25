from pyflix2 import *
from movie import movie
import ConfigParser
import os

class Netflix(object):
    """
    Netflix API
    """
    def __init__(self):
        section = 'netflix'
        config = ConfigParser.SafeConfigParser()
        config.readfp(open('config.conf'))
        if not config.has_section(section):
            raise ValueError('Config section {0} does not exists'.format(section))

        KEY=config.get(section,'KEY')
        SHARED_SECRET=config.get(section,'SHARED_SECRET')
        self.service = NetflixAPIV2('Where Is Movie', KEY, SHARED_SECRET)

    def get_movie_by_title(self, title, filter=None):
        '''
        Args:
            title - Title of the movie
            filter - streaming or dvd
        '''

        res = self.service.get_movie_by_title(title, filter=filter)
        m_details = self.service.get_title(res.get('id'), category="format_availability")
        m = movie(str(res.get('title')), 'Netflix')

        # Check for formats
        if m_details.get('delivery_formats'):
            f = m_details.get('delivery_formats')
            if f.get('DVD'):
                m.dvd = True
            if f.get('instant'):
                m.stream = True

        # return the movie dict
        return m
