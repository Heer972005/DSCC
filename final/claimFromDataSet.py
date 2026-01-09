import spacy

nlp = spacy.load("en_core_web_sm")

def extract_claim(sentence):
    sentence = str(sentence).lower()
    doc = nlp(sentence)

    opinion_words = [
        "useless", "lazy", "corrupt", "bad", "waste", "stupid", "weak",
        "always", "never", "worst", "best", "better than", "failed",
        "everyone", "nobody"
    ]

    medical_triggers = [
        "cure", "cures", "treat", "treats", "heal", "heals",
        "diabetes", "cancer", "infertility", "vaccine"
    ]

    is_medical = any(med in sentence for med in medical_triggers)
    is_opinion = any(word in sentence for word in opinion_words)

    # Only filter opinion if it is NOT medical
    if is_opinion and not is_medical:
        return None

    # Force extraction for medical claims
    if is_medical:
        pass

    subject = ""
    verb = ""
    obj = ""
    prep_phrase = ""

    for token in doc:
        if token.dep_ in ("nsubj", "nsubjpass"):
            subject = token.text
        if token.dep_ == "ROOT":
            verb = token.lemma_
        if token.dep_ in ("dobj", "attr"):
            obj = token.text
        if token.dep_ == "pobj":
            prep_phrase = token.text

    if "capital" in sentence and prep_phrase:
        obj = "capital of " + prep_phrase

    if "independence" in sentence and prep_phrase:
        obj = "independence in " + prep_phrase

    if subject and verb and (obj or prep_phrase):
        final_obj = obj if obj else prep_phrase
        return f"{subject} {verb} {final_obj}"
    else:
        return None
