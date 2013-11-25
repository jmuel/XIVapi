import unittest
from src.CharacterSearch import CharacterSearch


class CharacterSearchTest(unittest.TestCase):

    characterSearcher = None

    def setUp(self):
        characterSearcher = None

    def testGetUrlAddsPlusSigns(self):
        url = CharacterSearch.getUrl("Arn Eldgrimm")

        self.assertEqual("http://eu.finalfantasyxiv.com/lodestone/character/?q=Arn+Eldgrimm", url)

