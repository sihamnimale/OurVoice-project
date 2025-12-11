import sys
from pathlib import Path

# ensure `src` package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# also add backend to sys.path for absolute imports in backend modules
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from backend.d_clientside_main import hashtag_generation


def test_hashtag_recommendations():
    post = "I'm learning to code in Python!"
    return hashtag_generation(post), print("Status: OK")

# NB. this test function will ask if you want to generate hashtags from the sample post
test_hashtag_recommendations()