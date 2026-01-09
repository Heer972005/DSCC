def detect_domain(text):
    text = text.lower()

    health_keywords = ["vaccine", "cancer", "diabetes", "disease", "infertility", "medicine"]
    tech_keywords = ["python", "c", "programming", "software", "code", "algorithm"]
    history_keywords = ["independence", "war", "king", "empire", "colonial"]
    geography_keywords = ["capital", "mountain", "river", "country", "continent"]
    politics_keywords = ["democracy", "election", "government", "politician", "parliament"]
    education_keywords = ["education", "student", "learning", "school", "university"]

    for word in health_keywords:
        if word in text:
            return "health"

    for word in tech_keywords:
        if word in text:
            return "technology"

    for word in history_keywords:
        if word in text:
            return "history"

    for word in geography_keywords:
        if word in text:
            return "geography"

    for word in politics_keywords:
        if word in text:
            return "politics"

    for word in education_keywords:
        if word in text:
            return "education"

    return "general"


# Test
samples = [
    "Vaccines cause infertility",
    "Python does not support OOP",
    "India got independence in 1950",
    "Sydney is the capital of Australia",
    "Democracy has failed everywhere"
]

for s in samples:
    print(f"Text: {s}")
    print("Detected Domain:", detect_domain(s))
    print("-" * 40)

def get_source_for_domain(domain):
    source_map = {
        "health": "WHO",
        "technology": "GeeksForGeeks / Official Docs",
        "history": "Wikipedia / Britannica",
        "geography": "Wikipedia",
        "politics": "Government Sources",
        "education": "NCERT / UNESCO",
        "general": "Wikipedia"
    }

    return source_map.get(domain, "Wikipedia")


# Test routing
for s in samples:
    domain = detect_domain(s)
    source = get_source_for_domain(domain)
    print(f"Text: {s}")
    print("Domain:", domain)
    print("Source Selected:", source)
    print("-" * 40)
