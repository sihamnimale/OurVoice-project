import sys
from pathlib import Path

# ensure `src` package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# also add backend to sys.path for absolute imports in backend modules
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from backend.d_clientside_main import print_helper_func


def test_print_helper_public_feed(post_alice):
    return print_helper_func([post_alice]), print("Status: OK")

post_alice = [1, "alice", "Title", "This is a post", "public", 0, [], []]
test_print_helper_public_feed(post_alice)



def test_print_helper_username(post_bill, username):
    return print_helper_func(array=post_bill, username=username), print("Status: OK")

post_bill = [[2, "bill", "Title", "This is bill's post", "public", 1, ["alice"], ["#tag"]]]
username = "bill"

test_print_helper_username(post_bill, username)