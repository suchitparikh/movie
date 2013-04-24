class movie(object):
    '''
    The movie class with information about the movie title, and whether it is available
    to stream or as a dvd
    '''    
    def __init__(self, title, service):
        self.title = title
        self.service = service
        self.stream = False
        self.dvd = True
        self.price_stream = 0
        self.price_dvd = 0

    def __repr__(self):
        ret = {"Title": self.title, "Service": self.service}
        if self.stream:
            ret['Streaming'] = "True"
            ret['Stream_Price'] = self.price_stream
        if self.dvd:
            ret['DVD'] = "True"
            ret['DVD_Price'] = self.price_dvd
        return "{0}".format(ret)

