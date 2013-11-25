import unittest
from BeautifulSoup import BeautifulSoup
from src.CharacterParser import CharacterParser


class CharacterParserTest(unittest.TestCase):
    characterParser = None
    validBaseStats = {"Strength": "55", "Dexterity": "66", "Vitality": "11", "Intelligence": "22", "Mind": "33", "Piety": "44"}
    validOffensiveStats = {"Accuracy": "534", "Critical Hit Rate": "34", "Determination": "53"}
    validDefensiveStats = {"Defense": "735", "Parry": "508", "Magic Defense": "734"}

    def setUp(self):
        #this is a little odd so I'll just say that I'm overriding the constructor to bypass the urllib calls
        def CharacterParserInit(self):
            self.html = None

        setattr(CharacterParser, '__init__', CharacterParserInit)
        self.characterParser = CharacterParser()
        self.characterParser.soup = BeautifulSoup(self.htmlUnderTest)

    def testGracefulErrorOnElementNotFoundInGetStat(self):
        self.assertEqual(None, self.characterParser.getBaseStat("test"))

    def testBaseStats(self):
        self.assertEqual(self.validBaseStats["Strength"], self.characterParser.getBaseStats()["Strength"])
        self.assertEqual(self.validBaseStats["Dexterity"], self.characterParser.getBaseStats()["Dexterity"])
        self.assertEqual(self.validBaseStats["Vitality"], self.characterParser.getBaseStats()["Vitality"])
        self.assertEqual(self.validBaseStats["Intelligence"], self.characterParser.getBaseStats()["Intelligence"])
        self.assertEqual(self.validBaseStats["Mind"], self.characterParser.getBaseStats()["Mind"])
        self.assertEqual(self.validBaseStats["Piety"], self.characterParser.getBaseStats()["Piety"])

    def testOffensiveStats(self):
        self.assertEqual(self.validOffensiveStats["Accuracy"], self.characterParser.getOffensiveStats()["Accuracy"])
        self.assertEqual(self.validOffensiveStats["Critical Hit Rate"], self.characterParser.getOffensiveStats()["Critical Hit Rate"])
        self.assertEqual(self.validOffensiveStats["Determination"], self.characterParser.getOffensiveStats()["Determination"])

    def testDefensiveStats(self):
        self.assertEqual(self.validDefensiveStats["Defense"], self.characterParser.getDefensiveStats()["Defense"])
        self.assertEqual(self.validDefensiveStats["Parry"], self.characterParser.getDefensiveStats()["Parry"])
        self.assertEqual(self.validDefensiveStats["Magic Defense"], self.characterParser.getDefensiveStats()["Magic Defense"])



    htmlUnderTest = """ <ul>
                            <li class="str">55</li>
                            <li class="dex">66</li>
                            <li class="vit">11</li>
                            <li class="int">22</li>
                            <li class="mnd">33</li>
                            <li class="pie">44</li>
                        </ul>
                        <ul>
                            <li><span class="left">Accuracy</span><span class="right">534</span></li>
                            <li><span class="left">Critical Hit Rate</span><span class="right">34</span></li>
                            <li><span class="left">Determination</span><span class="right">53</span></li>
                        </ul>
                        <ul class="param_list">
                            <li class="clearfix"><span class="left">Defense</span><span class="right">735</span></li>
                            <li class="clearfix"><span class="left">Parry</span><span class="right">508</span></li>
                            <li class="clearfix"><span class="left">Magic Defense</span><span class="right">734</span></li>
                        </ul>

                        """
