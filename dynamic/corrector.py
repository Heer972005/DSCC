def generate_correction(claim, evidence, original_response):
    """
    Generates a corrected response based on evidence.
    If evidence is available, rewrite the response correctly.
    If not, return a safe fallback message.
    """

    if evidence is None:
        return "The information provided is incorrect or unverifiable. Please consult reliable sources."

    # Simple correction strategy: replace incorrect statement with evidence-based explanation
    correction = f"The earlier statement is incorrect. According to reliable sources: {evidence}"

    return correction
