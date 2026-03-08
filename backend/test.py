from analyser.url_detector import extract_urls
from analyser.heuristic import heuristic_score
from analyser.url_risk import url_risk_score

# checking for extracting of URL: 
email_1 = """
    please verify your account immediately:
    https://bit.ly/login-secure
    """

print(extract_urls(email_1))

# Checking of heuristic score: 
email_2 = """
    Dear customer, 

    your bank account has been suspended.
    Please verify your account immediately.
    Click here to login.
    
    """

score_1, keywords = heuristic_score(email_2)

print("Score: ", score_1)
print("keywords: ", keywords)

# Checking of URL risks like URL shortners: 

email_3 = """
    Dear user, 
    Your account has been suspended.
    Click here to verify immediately:
    https://bit.ly/secure-login
    """
urls = extract_urls(email_3)

score_2, issues = url_risk_score(urls)

print("URLs: ", urls)
print("URL Score: ", score_2)
print("Issues: ", issues)