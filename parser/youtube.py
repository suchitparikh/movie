#!/usr/bin/python

from apiclient.discovery import build
import ConfigParser
import json
import urllib

class Youtube(object):
    """
    Youtube API parser
    """
    section = "youtube"
    config = ConfigParser.SafeConfigParser()
    config.readfp(open('../config.cfg'))
    if not config.has_section(section):
        # error condition
        pass

    DEVELOPER_KEY = config.get(section, 'DEVELOPER_KEY')
    YOUTUBE_API_SERVICE_NAME = config.get(section, 'YOUTUBE_API_SERVICE_NAME')
    YOUTUBE_API_VERSION = "V3"

    def __init__(self):
        API_KEY = ""
        part = "contentDetails"
        fields = ""
