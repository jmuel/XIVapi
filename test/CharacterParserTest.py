import unittest
from src.CharacterParser import CharacterParser


class CharacterParserTest(unittest.TestCase):
    characterParser = None

    def setUp(self):
        self.characterParser = CharacterParser(self.htmlUnderTest)

    def testGracefulErrorOnElementNotFoundInGetStat(self):
        self.assertEqual(None, self.characterParser.getBaseStat("test"))

    def testBaseStats(self):
        self.assertEqual("55", self.characterParser.getBaseStats()["Strength"])
        self.assertEqual("55", self.characterParser.getBaseStats()["Strength"])
        self.assertEqual("66", self.characterParser.getBaseStats()["Dexterity"])
        self.assertEqual("11", self.characterParser.getBaseStats()["Vitality"])
        self.assertEqual("22", self.characterParser.getBaseStats()["Intelligence"])
        self.assertEqual("33", self.characterParser.getBaseStats()["Mind"])
        self.assertEqual("44", self.characterParser.getBaseStats()["Piety"])

    def testOffensiveStats(self):
        self.assertEqual("534", self.characterParser.getOffensiveStats()["Accuracy"])
        self.assertEqual("34", self.characterParser.getOffensiveStats()["Critical Hit Rate"])
        self.assertEqual("53", self.characterParser.getOffensiveStats()["Determination"])

    def testDefensiveStats(self):
        self.assertEqual("735", self.characterParser.getDefensiveStats()["Defense"])
        self.assertEqual("508", self.characterParser.getDefensiveStats()["Parry"])
        self.assertEqual("734", self.characterParser.getDefensiveStats()["Magic Defense"])



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
