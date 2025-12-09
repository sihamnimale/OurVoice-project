from unittest import TestCase, main
from src.backend.e_class_keyword_detection import KeywordDetection

class TestKeywordDetection(TestCase):

    def setUp(self):
        self.detector = KeywordDetection()

    def test_keywordtrigger_on_depression(self):
        content = "I’ve been so depressed lately that I can barely get out of bed."
        self.assertTrue(self.detector.detect_keywords(content))

    def test_keywordtrigger_on_eviction_risk(self):
        content = "I might get evicted next month and I’m really scared I could be on the verge of being homeless."
        self.assertTrue(self.detector.detect_keywords(content))

    def test_does_not_trigger_on_overwhelm(self):
        content = "Sometimes I feel overwhelmed being in tech as a woman, but I love the challenge."
        self.assertFalse(self.detector.detect_keywords(content))

    def test_does_not_trigger_on_financial_goal(self):
        content = "I want to start investing but I’m scared of getting it wrong."
        self.assertFalse(self.detector.detect_keywords(content))
    
if __name__ == '__main__':
    main()