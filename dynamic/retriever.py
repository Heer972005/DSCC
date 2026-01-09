import wikipedia

def retrieve_evidence(claim, max_sentences=3):
    """
    Retrieves summary evidence from Wikipedia for a given claim.
    Returns a short text snippet or None.
    """
    try:
        search_results = wikipedia.search(claim)

        if not search_results:
            return None

        page_title = search_results[0]
        page = wikipedia.page(page_title)

        summary = page.summary

        # Return only first few sentences to keep it clean
        sentences = summary.split(". ")
        evidence = ". ".join(sentences[:max_sentences])

        return evidence

    except wikipedia.exceptions.DisambiguationError as e:
        # Pick the first option if ambiguous
        try:
            page = wikipedia.page(e.options[0])
            summary = page.summary
            sentences = summary.split(". ")
            evidence = ". ".join(sentences[:max_sentences])
            return evidence
        except:
            return None

    except Exception:
        return None
