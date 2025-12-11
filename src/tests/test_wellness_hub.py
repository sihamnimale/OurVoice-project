import sys
from pathlib import Path

# ensure `src` package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.d_clientside_main import wellness_career_helper

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

def wellness_career_helper_test(resources=test_resources):
    return wellness_career_helper(resources), print("Status: OK")

wellness_career_helper_test(test_resources)
