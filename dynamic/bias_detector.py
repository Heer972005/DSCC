import re

# Keyword lists for different bias types
GENDER_BIAS = [
    "women are", "men are", "girls are", "boys are",
    "naturally better", "naturally worse", "bad drivers",
    "better leaders", "less intelligent"
]

SOCIAL_BIAS = [
    "poor people", "rich people", "villagers", "city people",
    "uneducated", "lazy", "dirty", "backward"
]

POLITICAL_BIAS = [
    "all politicians", "all governments", "all voters",
    "corrupt", "useless government", "failed democracy"
]

ETHICAL_BIAS = [
    "introverts are", "extroverts are", "fat people", "ugly people",
    "disabled people", "old people"
]

def detect_bias(text):
    text = str(text).lower()

    # Gender bias
    for phrase in GENDER_BIAS:
        if phrase in text:
            return 1, "gender"

    # Social / economic bias
    for phrase in SOCIAL_BIAS:
        if phrase in text:
            return 1, "social"

    # Political bias
    for phrase in POLITICAL_BIAS:
        if phrase in text:
            return 1, "political"

    # Ethical / personality bias
    for phrase in ETHICAL_BIAS:
        if phrase in text:
            return 1, "ethical"

    return 0, "none"
