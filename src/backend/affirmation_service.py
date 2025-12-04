#Write a program to send requests to the RAPID API and get affirmation posts from the API.
'''
PSEUDO CODE:
1, Send requests to the API based off category from user input.
2, Receive response and return affrimation to the user.
'''

import os
import requests
from dotenv import load_dotenv

load_dotenv()

#This is the website I am trying to reach.
API_HOST = "affirmations-api-by-apirobots.p.rapidapi.com"
BASE_URL = f"https://{API_HOST}/v1/affirmations"

#The credentials are being read from a different environment where the RAPIDAPI KEY is stored.
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

HEADERS = {
    "x-rapidapi-host": API_HOST,
    "x-rapidapi-key": RAPIDAPI_KEY
}
#This map is linking keywords with the category the API will get affrimations from. This is not the keyword and text-recognition logic.
KEYWORD_CATEGORY_MAP = {
    "depression": "health",
    "anxiety": "health",
    "sad": "happiness",
    "love": "love",
    "sleep": "sleep",
}

#Building the full URL that makes the default category happiness.
DEFAULT_CATEGORY = "happiness"

#This function is sending requests to get affrimations by the catgeory endpoint.
def get_random_affirmation(category = DEFAULT_CATEGORY):
    url = f"{BASE_URL}/categories/{category}/random"

    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        data = response.json()

        
        if isinstance(data, dict) and "affirmation" in data:
            return category, data["affirmation"]

        
        return category, response.text.strip()

    except Exception:
        return category, "You matter. Take a breath."
    
#This function is linking the keywords detected with the Category Map shown above.
def map_keywords_to_category(keywords):
    
    for kw in keywords:
        if kw.lower() in KEYWORD_CATEGORY_MAP:
            return KEYWORD_CATEGORY_MAP[kw.lower()]
    return None

#This function links the sends the request to the API and returns the results.
def get_affirmation_for_keywords(keywords, sentiment = None):
    
    # 1. Try using keywords
    category = map_keywords_to_category(keywords) if keywords else None

    # 2. If no category found, use default
    if not category:
        category = DEFAULT_CATEGORY

    # 3. Get affirmation text
    return get_random_affirmation(category)