from unittest import TestCase
from backend.g_class_affirmations import SentimentAnalysis, Affirmations

# Testing sentiment analysis correctly classifies user text as positive, negative or neutral as expected
class TestSentimentAnalysis(TestCase):

    def setUp(self):
        self.analyzer = SentimentAnalysis(label=None)

    def test_positive_text(self):
        text = "I finally feel proud of myself. I’m so grateful for how far I’ve come."
        label = self.analyzer.text_analysis(text)
        self.assertEqual(label, "Positive")

    def test_negative_text(self):
        text = "I feel completely drained and hopeless lately."
        label = self.analyzer.text_analysis(text)
        self.assertEqual(label, "Negative")

    def test_neutral_text(self):
        text = "I listened to a podcast today about investing while commuting..."
        label = self.analyzer.text_analysis(text)
        self.assertEqual(label, "Neutral")

# Testing that affirmation categories are selected based on the sentiment level
class TestAffirmations(TestCase):
    
    def setUp(self):
        self.affirm = Affirmations()

    # This tests that each sentiment type selects a category from the allowed list 
    def test_affirmation_positive_category(self):
        self.affirm.label = "Positive"
        cat =self.affirm.affirmation_category()
        self.assertIn(cat, ["love", "health", "beauty", "happiness", "money", "blessing"])

    def test_affirmation_negative_category(self):
        self.affirm.label = "Negative"
        cat =self.affirm.affirmation_category()
        self.assertIn(cat, ['gratitude', 'spiritual', 'blessing', 'sleep'])

    def test_affirmation_neutral_category(self):
        self.affirm.label = "Neutral"
        cat =self.affirm.affirmation_category()
        self.assertIn(cat, ['love', 'health', 'beauty', 'gratitude', 'spiritual', 'happiness', 'money', 'blessing', 'sleep'])
    