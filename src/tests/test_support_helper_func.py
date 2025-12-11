import sys
from pathlib import Path

# ensure `src` package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# also add backend to sys.path for absolute imports in backend modules
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from backend.d_clientside_main import support_hub_helper

test_resources = {
        "1": {
            "category": "First test category",
            "support":[
                        {"name" : "Printed Test"}, 
            ]
        },
        "2": {
            "category": "Second test category",
            "support": [
                        {"name" : "Printed Test"}, 
            ]
        }, 
        "3": {
            "category": "Third test category",
            "support": [
                        {"name" : "Printed Test"}, 
            ]
        }}

def support_hub_test(resources=test_resources):
    return support_hub_helper(resources), print("Status: OK")

support_hub_test(test_resources)