"""
This is Rule-based detection. It means even if Ai fails, the system
will still detect basic phishing signals.
"""


def heuristic_score(email_text):
    """
    Calculates phishing risks using the score based on suscipious keywords
    """

    suspicious_keywords = [
        "urgent",
        "verify your account",
        "password",
        "bank",
        "login immediately",
        "click here",
        "suspended",
        "security alert",
        "confirm your identity",
        "limited time"
    ]

    score = 0
    detected_keywords = []

    text = email_text.lower()

    for keywords in suspicious_keywords:
        if keywords in text:
            score += 10
            detected_keywords.append(keywords)
    
    return score, detected_keywords

