import urllib2
from src.CharacterParser import CharacterParser


class Parser:
    baseUrl = "http://eu.finalfantasyxiv.com/"

    def getCharacterData(self, id):
        url = self.baseUrl + "/lodestone/character/" + str(id)
        response = urllib2.urlopen(url)
        characterParser = CharacterParser(response)
        return characterParser.getAllStats()