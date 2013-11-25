from src.CharacterParser import CharacterParser
from test.unit.CharacterParserTest import CharacterParserTest


class CharacterParserTest(CharacterParserTest):

    characterId = 2385133

    def setUp(self):
        self.validBaseStats = {"Strength": "82", "Dexterity": "57", "Vitality": "80", "Intelligence": "16", "Mind": "30", "Piety": "21"}
        self.validOffensiveStats = {"Accuracy": "120", "Critical Hit Rate": "117", "Determination": "61"}
        self.validDefensiveStats = {"Defense": "173", "Parry": "122", "Magic Defense": "173"}
        self.characterParser = CharacterParser(self.characterId)
