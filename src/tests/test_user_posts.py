from unittest import TestCase, mock
from backend.d_clientside_main import get_username_entries

# Testing retrieving a user's post entries from their personal profile using mock API
class TestGetUserPosts(TestCase):

    @mock.patch("backend.d_clientside_main.requests.get")
    def test_get_username_entries_to_return_posts(self, mock_get):
        mock_response = mock.MagicMock()
        # Create a mock API with two user posts (private and public)
        mock_response.json.return_value = [
            {"post_id": 2,
             "username": "sally54",
             "title": "My second post",
             "post": "I am feeling blessed today",
             "private_public": "private"
            },
            {"post_id": 1,
             "username": "sally54",
             "title": "My first post",
             "post": "This is my first journal post",
             "private_public": "public"
            },
        ]
        mock_get.return_value = mock_response
        res = get_username_entries("sally54")
        # Test the correct API endpoint used
        mock_get.assert_called_once_with(
            "http://127.0.0.1:5001/sally54",
            headers={"content-type": "application/json"}
        )
        # Check returned data corresponds to correct user
        self.assertEqual(res[0]["username"], "sally54")