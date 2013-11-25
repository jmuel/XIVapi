import urllib2
from BeautifulSoup import BeautifulSoup

class CharacterParser:

    soup = None
    statList = {"Strength": "str", "Dexterity": "dex", "Vitality": "vit", "Intelligence": "int", "Mind": "mnd", "Piety": "pie"}
    offensiveStatList = ["Accuracy", "Critical Hit Rate", "Determination"]
    defensiveStatList = ["Defense", "Parry", "Magic Defense"]


    def __init__(self, characterId):
        html = self.__getHtml(characterId)
        self.soup = BeautifulSoup(html)

    def __getHtml(self, characterId):
        url = "http://eu.finalfantasyxiv.com/lodestone/character/" + str(characterId)
        return urllib2.urlopen(url)

    def getAllStats(self):
        statMap = dict()
        statMap["Base Stats"] = self.getBaseStats()
        statMap["OffensiveStats"] = self.getOffensiveStats()
        statMap["DefensiveSTats"] = self.getDefensiveStats()
        return statMap

    def getOffensiveStats(self):
        statMap = dict()
        for stat in self.offensiveStatList:
            statMap[stat] = self.getDerivedStat(stat)
        return statMap

    def getDefensiveStats(self):
        statMap = dict()
        for stat in self.defensiveStatList:
            statMap[stat] = self.getDerivedStat(stat)
        return statMap

    def getDerivedStat(self, stat):
        return self.soup.find(text=stat).parent.parent.find("span", {"class": "right"}).text

    def getBaseStats(self):
        statMap = dict()
        for key in self.statList:
            statMap[key] = self.getBaseStat(self.statList[key])
        return statMap

    def getBaseStat(self, stat):
        element = self.soup.find("li", {"class": stat})
        if element != None:
            return element.text
        else:
            return None