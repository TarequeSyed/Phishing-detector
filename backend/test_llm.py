from analyser.llm_detector import query_llm

prompt = "Explain phishing in one sentence."

response = query_llm(prompt)

print(response)