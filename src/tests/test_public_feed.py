import sys
from pathlib import Path

# ensure `src` package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# also add backend to sys.path for absolute imports in backend modules
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from unittest import TestCase, mock, main
from backend.d_clientside_main import get_public_feed

# Testing public feed API call returns data correctly
class TestGetPublicFeed(TestCase):

    @mock.patch("backend.d_clientside_main.requests.get")
    def test_get_public_feed_returns_posts(self, mock_get):
        mock_response = mock.MagicMock()
        # Create a mock API response
        mock_response.json.return_value = [
            {"post_id": 1,
             "username": "usertest001",
             "title": "My first post",
             "post": "This is my journal post",
             "private_public": "public",
             "likes": 0,
             "user_likes": "",
             "hashtags": "#mock"}
        ]

        mock_get.return_value = mock_response
        res = get_public_feed()

        mock_get.assert_called_once_with(
            "http://127.0.0.1:5001/feed",
            headers={"content-type": "application/json"}
        )
        # Tests that the returned data matches the mock response
        self.assertEqual(res[0]['post'], "This is my journal post")

if __name__ == "__main__":
    main() 