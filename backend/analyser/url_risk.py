import ipaddress
from urllib.parse import urlparse

def url_risk_score(urls):
    """
    Analyse URLs for Phishing indicators
    """

    suspicious_shortners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "ow.ly"
    ]

    score = 0
    detected_issues = []

    for url in urls:
        parsed = urlparse(url)
        domain = parsed.hostname
        # it will check for shortner link: 
        for shortner in suspicious_shortners:
            if shortner in urls:
                score += 25
                detected_issues.append(f"shortened URL: {url}")

        # for '@' symbol:
        if "@" in url:
            score += 20
            detected_issues.append(f"Suspicious '@' in url: {url}")

        # for ip based domain:
        try:
            ip = ipaddress.ip_address(domain)

            if ip.is_private:
                # it is local network, then ignore
                pass
            else:
                score += 30
                detected_issues.append(f"Public IP URL: {url}")
        except:
            # it is not a IP address
            pass

    return score, detected_issues