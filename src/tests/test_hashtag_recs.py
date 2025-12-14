import sys
from pathlib import Path
from unittest import TestCase, main

# ensure `src` package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# also add backend to sys.path for absolute imports in backend modules
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from backend.d_clientside_main import HashtagRecs

class TestHashtags(TestCase):

    def setUp(self):
        self.hashtags = HashtagRecs()

    # This test checks that the hashtag class would generate hashtags for keywords in a user's post entry
    def test_keywordtrigger_on_depression(self):
        content = "I’ve been so happy lately that I can't wait to get up in the morning."
        keywords = self.hashtags.extract_keywords(content)
        self.assertTrue(self.hashtags.generate_hashtags(keywords))        

if __name__ == "__main__":
    main()