import spacy

nlp = spacy.load("en_core_web_sm")

def extract_claim(sentence):
    doc = nlp(sentence)
    subject = None
    verb = None
    obj = None

    for token in doc:
        if token.dep_ in ("nsubj", "nsubjpass"):
            subject = token.text
        if token.dep_ == "ROOT":
            verb = token.text
        if token.dep_ in ("dobj", "attr", "pobj"):
            obj = token.text

    if subject and verb and obj:
        return f"{subject} {verb} {obj}"
    else:
        return None


# Test
s = "Albert Einstein invented the telephone."
print(extract_claim(s))
