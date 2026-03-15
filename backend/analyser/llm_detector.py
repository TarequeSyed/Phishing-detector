import re
import requests # for the api call
import os
from dotenv import load_dotenv
load_dotenv()
HF_TOKEN = os.getenv("HF_API_KEY")


# For Strict structured output function: 
def build_prompts(email_text, urls):
    prompt = f"""
    You are a Cybersecurity analyst specializing in phishing detection.
    
    Analze the following email for phishing indicators.
    
    Look for these signs:
    - urgent requests
    - credential harvesting
    - financial scams
    -suspicious links
    - impersonation of trusted companies
    - generic greetings
    
    Email Content:
    {email_text}

    Extracted URLs:
    {urls}

    Respond ONLY in this format:
    
    Risk score: <0-100>
    
    Indicators:
    - Indicators 1
    - Indicators 2
    - Indicators 3
    
    Explanations:
    Short explanation of why the email is suspicious or safe.
    """

    return prompt

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def query_llm(prompt):
    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.2
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    data = response.json()

    text = data["choices"][0]["message"]["content"]

    return text

def parse_risk_score(text):
    match = re.search(r"Risk\s*score\s*:\s*(\d+)", text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 0

# Combining all three functions: 

def llm_score(email_text, urls):

    # it will build the prompt:
    prompt = build_prompts(email_text, urls)

    # now, we will send the prompt to llms:
    response_text = query_llm(prompt)

    # we will extract the risk score:
    score = parse_risk_score(response_text)

    return score, response_text