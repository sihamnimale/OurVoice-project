import string

class KeywordDetection:
    # list predefined keywords to trigger our support hub 
    def __init__(self):
        self.keywords = [
        "anxiety","panic","unease", "anxious", "overwhelmed","fear",
        "depression","lonely","suicidal","worthless", "disorder",
        "eating", "self-harm", "regret", "homelessness", "harassment"
        ]

    # this function goes through the post content and removes any punctuations which then converts to a list
    # and finds keywords in the list that detects keywords that could indicate support needed
    def detect_keywords(self, content):
        # convert to lowercase
        content = content.lower()
        #remove punctuation
        content = content.translate(str.maketrans("", "", string.punctuation))

        # split into words
        words = content.split()

        # check for any matching keywords
        for keyword in self.keywords:
            if keyword in words:
                return True
            
        return False
    
