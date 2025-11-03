def keyword_risk_detection(text):
    risky_terms = ["termination", "liability", "non-compete", "breach", "penalty"]
    found = [term for term in risky_terms if term in text.lower()]
    return {"risk_terms": found, "risk_level": "High" if found else "Low"}