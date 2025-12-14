# Nltk is a suite of natural language libraries and programes. There are many things you can do with NLTK
# but for this task we have decided to use it for hashtag recommendations.
import nltk

class HashtagRecs:
    """
    A small helper class that creates hashtag suggestions for users.
    It does this by:
    - analysing their post,
    - extracting important words (nouns + adjectives),
    - converting those words into hashtag form.
    """
    def __init__(self):
        self.hashtags = []

    # This function uses nltk to analyse the user's post to extract keywords from it and return a string of the keywords.
    def extract_keywords(self, content):
        """
        Identifies key words from the user's writing using NLTK.
        STEPS:
        1. Break the text into individual words (tokenising).
        2. Ask NLTK to label each word with its part of speech (noun, proper noun, adjective.).
        3. Keep only meaningful words like:
            - NN  → noun (e.g., "stress", "friendship")
            - NNP → proper noun (e.g., "London", "January")
            - JJ  → adjective (e.g., "tired", "overwhelmed")
        Returns:
            A list of keywords that represent the main themes of the post.
        """
        # The word_tokenize function splits the content into a list of words and punctuation.
        tokens = nltk.word_tokenize(content) 
        # The pos_tag function then takes the tokenized content and adds a tag to each string tags is therefore
        # a list of tuples, the first element being a string from the content and the second being a tab
        tags = nltk.pos_tag(tokens) 
        # Keywords is a list of the strings that have particular tags, e.g. "NN" denotes a singular noun
        keywords = [word for (word, tag) in tags if tag.startswith('NN') or tag == 'JJ' or tag == 'NNP']
        return keywords
    
    # This function takes the keywords and puts them into the class's one atrribute, which is a list called hashtags.
    def generate_hashtags(self, keywords):
        """
        Converts the extracted keywords into simple hashtag suggestions.
        Example:
            keywords = ["stress"]
            → hashtags = ["#stress"]
        - Hashtags are stored in lowercase for consistency.
        - Duplicates are removed.
        Returns:
            A list of hashtag strings.
        """
        hashtags = ['#' + keyword.lower() for keyword in keywords]
        # Convert to a set to remove duplicates, then back to a list.
        self.hashtags = list(set(hashtags))
        return self.hashtags
