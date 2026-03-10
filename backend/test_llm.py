from analyser.llm_detector import llm_score
from analyser.url_detector import extract_urls
import requests
email = "Your account is suspended. Click on the link: https:bit.ly/login"

url = extract_urls(email)
score, explanation = llm_score(email, ["url"])

print(score)
print(explanation)