#The functions are from the sentiment and affirmation service files are being imported to be used in this file.
from sentiment_service import text_analysis
from affirmation_service import get_affirmation_for_keywords

#
def process_entry(text):
    
    # 1) Analyze sentiment
    s = text_analysis (text)  #Expects {'Sentiment': 'Positive'|'Neutral'|'Negative', 'compound': float}

    # 2) Get an affirmation: we call the helper which accepts keywords and sentiment.
    # Since keywords module isn't ready, this passes an empty list and the sentiment.
    category, affirmation = get_affirmation_for_keywords([], s["sentiment"])

    # 3) Return a small structured result
    return {
        "sentiment": s["sentiment"],
        "compound": s["compound"],
        "affirmation": affirmation,
        "affirmation_category": category
    }