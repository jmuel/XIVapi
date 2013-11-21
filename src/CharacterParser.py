from BeautifulSoup import BeautifulSoup

class CharacterParser:

    soup = None
    statList = {"Strength": "str", "Dexterity": "dex", "Vitality": "vit", "Intelligence": "int", "Mind": "mnd", "Piety": "pie"}
    offensiveStatList = ["Accuracy", "Critical Hit Rate", "Determination"]
    defensiveStatList = ["Defense", "Parry", "Magic Defense"]


    def __init__(self, html):
        self.soup = BeautifulSoup(html)

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