import sys
from pathlib import Path

# ensure `src` package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from unittest import TestCase, main
from backend.f_class_hashtag_recs import HashtagRecs


class TestHashtagRecs(TestCase):

    def setUp(self):
        self.recs = HashtagRecs()

    def test_initial_hashtags_empty(self):
        self.assertEqual(self.recs.hashtags, [])

    def test_generate_hashtags_lowercase_unique(self):
        keywords = ['Happy', 'python', 'happy']
        tags = self.recs.generate_hashtags(keywords)

        # tags should be a list with lowercase, unique hashtags
        self.assertIsInstance(tags, list)
        self.assertEqual(set(tags), {'#happy', '#python'})


if __name__ == '__main__':
    main()