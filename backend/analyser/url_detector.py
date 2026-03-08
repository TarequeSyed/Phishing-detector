import re

def extract_urls(text):
    """ 
    Extract all the urls from the text
    """
    url_pattern = r'https?://\S+'
    urls = re.findall(url_pattern, text)

    return urls