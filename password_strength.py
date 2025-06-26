import re

def analyze_password(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short (use at least 8 characters)")
    if not re.search(r"[A-Z]", password):
        issues.append("No uppercase letter")
    if not re.search(r"[a-z]", password):
        issues.append("No lowercase letter")
    if not re.search(r"[0-9]", password):
        issues.append("No digit")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("No special character")
    if issues:
        return "Weak Password", issues
    else:
        return "Strong Password", []
