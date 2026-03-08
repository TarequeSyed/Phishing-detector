from analyser.url_detector import extract_urls
from analyser.heuristic import heuristic_score

email = """
    please verify your account immediately:
    https://bit.ly/login-secure
    """

print(extract_urls(email))

email = """
    Dear customer, 

    your bank account has been suspended.
    Please verify your account immediately.
    Click here to login.
    
    """

score, keywords = heuristic_score(email)

print("Score: ", score)
print("keywords: ", keywords)