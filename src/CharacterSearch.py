import urllib2


class CharacterSearch:

    html = None

    def __init__(self, url):
        html = urllib2.urlopen(url)