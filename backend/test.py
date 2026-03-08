from analyser.url_detector import extract_urls

email = """
    please verify your account immediately:
    https://bit.ly/login-secure
    """

print(extract_urls(email))