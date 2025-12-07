#Writing a function to analyze text using the sentiment analyzer API and assign labels to the text based off the scoring from the analysis
'''
PSEUDO CODE:
1, Receiving the text presented. - Import VaderSentiment and then defined a function that accepts a text parameter.
2, Analyse the text presented. - Send to the API and receive a score between 1 and -1.
3, Assign labels to the text presented. - Use elif for range and labels.
4, Return label and score. 
'''

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def text_analysis(text):
    score = analyzer.polarity_scores(text) #This returns a dictionary
    compound_score = score["compound"]
    if compound_score >= 0.05:
        label = "Positive"
    elif compound_score <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return {'sentiment' : label, 'compound' : compound_score}


