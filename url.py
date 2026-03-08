import re

def extract_urls(text):
    url_pattern = r'https?://\S+'
    return re.findall(url_pattern, text)

def heuristic_score(text):
    suspicious_words = [
        'urgent', 
        'compromised',
        'bank',
        'password',
        'limited time',
        'login immediately',
        'suspended account'
    ]

    score = 0
    for words in suspicious_words:
        if words.lower() in text.lower():
            score += 10
    return score