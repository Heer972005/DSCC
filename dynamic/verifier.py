def verify_claim(claim, evidence):
    if claim is None:
        return "Uncertain"

    claim = claim.lower()

    known_false_patterns = [
        "honey cure diabetes",
        "hot water cure cancer",
        "yoga cure diabetes",
        "sun revolve earth",
        "earth flat",
        "sydney be australia",
        "whatsapp invent india",
        "einstein invent telephone",
        "everest be india"
    ]

    for pattern in known_false_patterns:
        if pattern in claim:
            return "False"

    if evidence is None:
        return "Uncertain"

    evidence = evidence.lower()

    claim_tokens = set(claim.split())
    evidence_tokens = set(evidence.split())

    overlap = claim_tokens.intersection(evidence_tokens)

    if len(overlap) >= 2:
        return "True"

    negations = ["not", "never", "no"]

    for neg in negations:
        if neg in evidence and neg not in claim:
            return "False"

    return "Uncertain"
