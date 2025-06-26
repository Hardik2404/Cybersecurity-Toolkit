import re
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = ["verify your account", "urgent", "password", "click below", "account suspended"]
DANGEROUS_DOMAINS = ["bit.ly", "tinyurl", "g00gle.com", "secure-paypal.com"]
DANGEROUS_EXTENSIONS = [".exe", ".bat", ".scr", ".js"]

def analyze_email(text):
    issues = []

    for word in SUSPICIOUS_KEYWORDS:
        if word.lower() in text.lower():
            issues.append(f"Suspicious keyword: '{word}'")

    links = re.findall(r'https?://[^\s]+', text)
    for link in links:
        parsed = urlparse(link)
        for bad_domain in DANGEROUS_DOMAINS:
            if bad_domain in parsed.netloc:
                issues.append(f"Suspicious link: {link}")

    for ext in DANGEROUS_EXTENSIONS:
        if ext in text:
            issues.append(f"Dangerous attachment: {ext}")

    result = "Likely Phishing" if len(issues) >= 2 else "Looks Safe"
    return result, issues