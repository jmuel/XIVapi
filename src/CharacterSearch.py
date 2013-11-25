import urllib2


class CharacterSearch:

    html = None

    def __init__(self, characterName):
        url = self.getUrl(characterName)
        html = urllib2.urlopen(url)

    @staticmethod
    def getUrl(characterName):
        characterName = characterName.replace(" ", "+")
        url = "http://eu.finalfantasyxiv.com/lodestone/character/"
        url += "?q=" + characterName
        return url