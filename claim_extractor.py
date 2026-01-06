import re

def extract_claims(text):
    # Convert to lowercase for uniformity
    text = text.lower()

    # Split on sentence enders
    sentences = re.split(r'[.!?]', text)

    claims = []

    for sentence in sentences:
        # Split on conjunctions
        parts = re.split(r'\band\b|\bbut\b|\bbecause\b|\bso\b', sentence)
        for part in parts:
            clean = part.strip()
            if len(clean) > 3:
                claims.append(clean)

    return claims


# Test
sample_text = "Yes, poor people are lazy and they don’t work hard because they avoid responsibility."
extracted = extract_claims(sample_text)

print("Extracted Claims:")
for c in extracted:
    print("-", c)
