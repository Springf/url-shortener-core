import re

"""
Implements a "very" basic regular expression based validator for the URL.
In real world more sophisticated approach could be taken:
1. parse the URL using the RFC standard to ensure the URL is valid.
2. Check against a scam registry to prevent scam URLs.
"""

def validate(url:str) -> bool:
    #for local testing purpose, localhost is intentionally added
    pattern = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?(?:localhost(:[0-9]{1,5})?(\/.*)?|[a-z0-9]+([\-\._]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?)$'
    return re.search(pattern, url) is not None
