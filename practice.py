"""Trying different edge cases here:
    like, 
    1. what if it is private network, because ip based url will be safish but that can't be
    said for public."""
def url_checker(urls):
    score = 0
    ip_based_url = []
    for url in urls:
        if "https://" in url or "http://" in url:
            domain_checker = url.split("//")[1].split("/")[0]
            if domain_checker.replace(".", "").isdigit():
                score += 30
                ip_based_url.append(f"Ip based: {url}")
    return score, ip_based_url
            
hello = ["https://192.168.01.01/login"]
score, link = url_checker(hello)

print("score", score)
print("bad link: ", link)