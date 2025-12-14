from unittest import TestCase
from backend.e_class_keyword_detection import KeywordDetection

# Testing the keyword detection function to correctly detect serious keywords in a user's post entry
# so support can be suggested when needed

class TestKeywordDetection(TestCase):

    def setUp(self):
        self.detector = KeywordDetection()

    # This test checks that specific keywords would trigger support in a user's post entry
    def test_keywordtrigger_on_depression(self):
        content = "I’ve been so depressed lately that I can barely get out of bed."
        self.assertTrue(self.detector.detect_keywords(content))

    def test_keywordtrigger_on_eviction_risk(self):
        content = "I might get evicted next month and I’m really scared I could be on the verge of being homeless."
        self.assertTrue(self.detector.detect_keywords(content))

    # This tests keywords that would not trigger or flag support in a user's post entry
    def test_does_not_trigger_on_overwhelm(self):
        content = "Sometimes I feel overwhelmed being in tech as a woman, but I love the challenge."
        self.assertFalse(self.detector.detect_keywords(content))

    def test_does_not_trigger_on_financial_goal(self):
        content = "I want to start investing but I’m scared of getting it wrong."
        self.assertFalse(self.detector.detect_keywords(content))
