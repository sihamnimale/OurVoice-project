# nltk is a suite of natural language libraries and programes. There are many things you can do with NLTK
# but for this task we have decided to use it for hashtag recommendations
import nltk

class HashtagRecs:
    def __init__(self):
        self.hashtags = []

    # this function uses nltk to analyse the user's post to extract keywords from it and return a string of the keywords
    def extract_keywords(self, content):
        # the word_tokenize function splits the content into a list of words and punctuation
        tokens = nltk.word_tokenize(content) 
        # the pos_tag function then takes the tokenized content and adds a tag to each string tags is therefore 
        # a list of tuples, the first element being a string from the content and the second being a tab
        tags = nltk.pos_tag(tokens) 
        # keywords is a list of the strings that have particular tags, e.g. "NN" denotes a singular noun
        keywords = [word for (word, tag) in tags if tag.startswith('NN') or tag == 'JJ' or tag == 'NNP']
        return keywords
    
    # this function takes the keywords and puts them into the class's one atrribute, which is a list called hashtags
    def generate_hashtags(self, keywords):
        self.hashtags = ['#' + keyword.lower() for keyword in keywords]
        return self.hashtags



nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')