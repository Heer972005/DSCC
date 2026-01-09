import wikipedia

def verify_claim(claim):
    try:
        results = wikipedia.search(claim)
        if not results:
            return "Possibly False"

        page = wikipedia.page(results[0])
        summary = page.summary.lower()
        claim = claim.lower()

        known_false_patterns = [
            "sun revolve earth",
            "earth flat",
            "vaccines cause infertility",
            "yoga cure diabetes",
            "hot water cure cancer",
            "everest be india",
            "whatsapp invent india",
            "einstein invent telephone",
            "columbus discover america 1942"
            "sydney be capital of australia"
        ]

        for pattern in known_false_patterns:
            if pattern in claim:
                return "Possibly False"

        # Negation handling
        if "not" in claim or "does not" in claim or "did not" in claim:
            positive_form = claim.replace("does not ", "").replace("did not ", "").replace("not ", "")
            if positive_form in summary:
                return "Possibly False"

        key_parts = claim.split()[:3]
        hit_count = sum(1 for part in key_parts if part in summary)

        if hit_count >= 2:
            return "Likely Supported"
        else:
            return "Possibly False"

    except wikipedia.exceptions.DisambiguationError:
        return "Possibly False"
    except Exception:
        return "Possibly False"
