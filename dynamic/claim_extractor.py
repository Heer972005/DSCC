import spacy

nlp = spacy.load("en_core_web_sm")

def extract_claim(text):
    text = str(text).lower()

    # Handle numeric factual patterns
    if text.startswith("there are"):
        return text.replace("there are", "").strip()

    doc = nlp(text)

    subject = ""
    verb = ""
    obj = ""

    for token in doc:
        if token.dep_ in ("nsubj", "nsubjpass"):
            subject = token.text
        if token.dep_ == "ROOT":
            verb = token.lemma_
        if token.dep_ in ("dobj", "attr", "pobj"):
            obj = token.text

    if subject and verb and obj:
        return f"{subject} {verb} {obj}"
    else:
        return None
