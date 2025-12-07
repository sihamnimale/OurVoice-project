import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # a module to provide us with a sentiment score of a user's post
import random

# firstly, we have written a class with a method to analyze text using a sentiment analyzer module called vaderSentiment 
# to assign the labels positive, negative or neutral to the text with this label, we will then be able to provide 
# personalised affirmations to our users.
'''
PSEUDO CODE FOR THE SENTIMENT ANALYSIS:
1, Receiving the text presented. - Import VaderSentiment and then defined a function that accepts a text parameter.
2, Analyse the text presented. - Send to the API and receive a score between 1 and -1.
3, Assign labels to the text presented. - Use elif for range and labels.
4, Return label and score. 
'''

class SentimentAnalysis:
    def __init__(self, label):
        self.analyzer = SentimentIntensityAnalyzer()
        self.label = None

    def text_analysis(self, text):
        score = self.analyzer.polarity_scores(text) # This returns a dictionary
        compound_score = score["compound"]
        if compound_score >= 0.05:
            self.label = "Positive"
        elif compound_score <= -0.05:
            self.label = "Negative"
        else:
            self.label = "Neutral"
        
        return self.label

# secondly, we have writen a further class to send requests to RAPID API, which is an API which provides affirmations
# that have been catagorised by things like love, health, happiness. The labels returned from the sentiment correspond
# with different affirmation categories, to make them more personalised to the user's mood.
'''
PSEUDO CODE FOR THE AFFIRMATION API:
1, Send requests to the API based off category from user input.
2, Receive response and return affrimation to the user.
'''

API_HOST = "affirmations-api-by-apirobots.p.rapidapi.com"
BASE_URL = "https://affirmations-api-by-apirobots.p.rapidapi.com/v1/affirmations/categories"
RAPIDAPI_KEY = "b21a953101msh7445d792fd7914bp108e8ejsnea5d5fa417ba"

headers = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": API_HOST
}

# this class has a method to send requests to get affrimations by the catgeory endpoint.
class Affirmations(SentimentAnalysis):
    def __init__(self):
        super().__init__(self)

    def affirmation_category(self):
        if self.label == "Positive":
            cats = ["love", "health", "beauty", "happiness", "money", "blessing"]
        elif self.label == "Negative":
            cats = ['gratitude', 'spiritual', 'blessing', 'sleep']
        else:
            cats = ['love', 'health', 'beauty', 'gratitude', 'spiritual', 'happiness', 'money', 'blessing', 'sleep']
        return random.choice(cats)

    def get_affirmation(self, category):
        try:
            url = f"{BASE_URL}/{category}/random"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            res = response.json()
            return res["text"]

        except Exception as e:
            print("Error with API service, apologies.", e)
            return "All is good. Take a breath, you matter"

    def personalised_affirmation(self, text):
        self.text_analysis(text)
        category = self.affirmation_category()
        return self.get_affirmation(category)


aff = Affirmations()
print(aff.personalised_affirmation("life is but a dream"))