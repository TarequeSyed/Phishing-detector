import ipaddress
from urllib.parse import urlparse


def url_risk_score(urls):
    """
    Analyse URLs for phishing indicators
    """

    suspicious_shorteners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "rebrand.ly",
        "buff.ly"
    ]

    score = 0
    detected_issues = []

    for url in urls:

        parsed = urlparse(url)
        domain = parsed.hostname

        if not domain:
            continue

        # ---- Shortened URL detection ----
        for shortener in suspicious_shorteners:
            if shortener in domain:
                score += 25
                detected_issues.append(f"Shortened URL detected: {url}")
                break

        # ---- '@' symbol in URL ----
        if "@" in url:
            score += 20
            detected_issues.append(f"Suspicious '@' in URL: {url}")

        # ---- IP address based URL ----
        try:
            ip = ipaddress.ip_address(domain)

            if not ip.is_private:
                score += 30
                detected_issues.append(f"Public IP URL detected: {url}")

        except ValueError:
            # Not an IP address
            pass

    return score, detected_issues