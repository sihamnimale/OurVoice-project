import string

class KeywordDetection:
    """
    A small helper class that scans a user's journal entry
    for words linked to distress, crisis or wellbeing concerns.

    If any of these words appear (even partially, like "depress" -> "depressed"),
    the app gently suggests visiting the Support Hub.
    """
    # high-risk/crisis-focused words to trigger to our support hub 
    def __init__(self):
        """
        A list of keyword stems we check for.
        Stems are used (e.g., 'depress', 'anxiet') so that different versions
        of a word can still be recognised.
        """
        self.keywords = [
        "abortion", "abus", "anorexi", "anxiet", "addict", "assault", "beat", "bulimia", "crisis", "debt", "depress", 
        "discriminat", "disorder", "die", "evict", "forced", "guilt", "harass", "homeless", "hopeless", "infertil",  
        "kill", "miscarriage", "numb", "panic", "rape", "regret", "selfharm", "starv", "suicid", "unemploye", 
        "unsafe", "violen"
        ]

    # This function goes through the post content and removes any punctuations which then converts to a list
    # and finds keywords in the list that detects keywords that could indicate support needed
    def detect_keywords(self, content):
        # Convert to lowercase.
        content = content.lower()
        # Remove punctuation
        content = content.translate(str.maketrans("", "", string.punctuation))

        # Split into words
        words = content.split()

        # Check for any matching keywords
        for word in words:
            for keyword in self.keywords:
                if word.startswith(keyword):
                    return True
            
        return False
    
