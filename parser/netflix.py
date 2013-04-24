from pyflix2 import NetflixAPIV2
from movie import movie

class Netflix(object):
    """
    Netflix API
    """
    def __init__(self):
        self.service = NetflixAPIV2('Where Is Movie', '', '')

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
