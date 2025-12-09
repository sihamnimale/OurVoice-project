import string

class KeywordDetection:
    # high-risk/crisis-focused words to trigger to our support hub 
    def __init__(self):
        self.keywords = [
        "abortion", "abus", "anorexi", "anxiet", "addict", "assault", "beat", "bulimia", "crisis", "debt", "depress", 
        "discriminat", "disorder", "die", "evict", "forced", "guilt", "harass", "homeless", "hopeless", "infertil",  
        "kill", "miscarriage", "numb", "panic", "rape", "regret", "selfharm", "starv", "suicid", "unemploye", 
        "unsafe", "violen"
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
        for word in words:
            for keyword in self.keywords:
                if word.startswith(keyword):
                    return True
            
        return False
    
