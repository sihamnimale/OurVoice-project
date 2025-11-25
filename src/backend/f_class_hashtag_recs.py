# THIS FILE NEEDS MORE WORK TO MAKE IT INTO A FUNCTIONING CLASS CAPABLE OF INTERACTING WITH
# THE CLIENTSIDE/MAIN FILE

import nltk

def downloads():
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('averaged_perceptron_tagger_eng')

class HashtagRecs:
    def extract_keywords(content):
        # Use NLTK to extract keywords from content
        tokens = nltk.word_tokenize(content)
        tags = nltk.pos_tag(tokens)
        keywords = [word for (word, tag) in tags if tag.startswith('NN') or tag == 'JJ' or tag == 'NNP']
        return keywords

    def generate_hashtags(keywords):
        # Generate hashtags from keywords
        hashtags = ['#' + keyword.lower() for keyword in keywords]
        return hashtags

    # Prompt the user to enter content
    content = input("Enter the content you want to generate hashtags for: ")

    # Extract keywords and generate hashtags
    keywords = extract_keywords(content)
    hashtags = generate_hashtags(keywords)

    # Print the resulting hashtags
    print("Generated hashtags:")
    for hashtag in hashtags:
        print(hashtag)