from pyflix2 import NetflixAPIV2
from movie import movie
import ConfigParser
import os

class Netflix(object):
    """
    Netflix API
    """
    
    section = 'netflix'
    config = ConfigParser.SafeConfigParser()
    config.readfp(open('../config.cfg'))
    if not config.has_section(section):
        # error condition
        pass

    KEY=config.get(section,'KEY')
    SHARED_SECRET=config.get(section,'SHARED_SECRET')

    def __init__(self):
        self.service = NetflixAPIV2('Where Is Movie', KEY, SHARED_SECRET)

    def get_movie_by_title(self, title, filter=None):
        '''
        Args:
            title - Title of the movie
            filter - streaming or dvd
        '''
        res = self.service.get_movie_by_title(title, filter=filter)
        m_details = self.service.get_title(res.get('id'), category="format_availability")

        print '\n{0}\n'.format(m_details)
        m = movie(str(res.get('title')), 'Netflix')

        # Check for formats
        if m_details.get('delivery_formats'):
            f = m_details.get('delivery_formats')
            if f.get('DVD'):
                m.DVD = True
            if f.get('instant'):
                m.stream = True

        # return the movie json
        return m
