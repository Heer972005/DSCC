import wikipedia

def verify_claim(claim):
    try:
        results = wikipedia.search(claim)
        if not results:
            return "No evidence found"

        page = wikipedia.page(results[0])
        summary = page.summary.lower()

        # simple heuristic: check if main keywords appear
        keywords = claim.split()[:3]

        if all(word in summary for word in keywords):
            return "Likely Supported"
        else:
            return "Possibly False"

    except wikipedia.exceptions.DisambiguationError:
        return "Ambiguous"
    except Exception:
        return "Verification Error"
