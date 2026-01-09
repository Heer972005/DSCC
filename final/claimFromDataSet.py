import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

'''# Claim extraction function
def extract_claim(sentence):
    doc = nlp(str(sentence))
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
'''
'''
def extract_claim(sentence):
    doc = nlp(str(sentence))
    subject = ""
    verb = ""
    obj = ""

    for token in doc:
        # subject
        if token.dep_ in ("nsubj", "nsubjpass"):
            subject = token.text

        # main verb
        if token.dep_ == "ROOT":
            verb = token.lemma_

        # object or attribute
        if token.dep_ in ("dobj", "attr", "pobj"):
            obj = token.text

    # filter bias/opinion sentences
    opinion_keywords = ["useless", "lazy", "corrupt", "bad", "waste"]
    for word in opinion_keywords:
        if word in sentence.lower():
            return None

    if subject and verb and obj:
        return f"{subject} {verb} {obj}"
    else:
        return None
'''

'''
def extract_claim(sentence):
    doc = nlp(str(sentence).lower())

    # Filter obvious opinion/bias sentences
    opinion_words = ["useless", "lazy", "corrupt", "bad", "waste", "stupid", "weak"]
    for word in opinion_words:
        if word in sentence.lower():
            return None

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

        # capture prepositional objects like "capital of Australia"
        if token.dep_ == "pobj":
            prep_phrase = token.text

    # Special handling for patterns like "capital of X", "independence in X"
    if "capital" in sentence.lower():
        for token in doc:
            if token.text == "capital":
                obj = "capital of " + prep_phrase

    if "independence" in sentence.lower():
        obj = "independence in " + prep_phrase

    if subject and verb and (obj or prep_phrase):
        final_obj = obj if obj else prep_phrase
        return f"{subject} {verb} {final_obj}"
    else:
        return None
'''
def extract_claim(sentence):
    sentence = str(sentence).lower()
    doc = nlp(sentence)

    # Strong opinion / bias filter
    opinion_words = [
        "useless", "lazy", "corrupt", "bad", "waste", "stupid", "weak",
        "always", "never", "worst", "best", "better than", "failed",
        "everyone", "nobody"
    ]

    for word in opinion_words:
        if word in sentence:
            return None

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

    # Handle special factual patterns
    if "capital" in sentence and prep_phrase:
        obj = "capital of " + prep_phrase

    if "independence" in sentence and prep_phrase:
        obj = "independence in " + prep_phrase

    if subject and verb and (obj or prep_phrase):
        final_obj = obj if obj else prep_phrase
        return f"{subject} {verb} {final_obj}"
    else:
        return None

# Load dataset
df = pd.read_excel(r"G:\vs\DSCC\final\hallucination_bias_dataset11.xlsx")

print(df.head())
print(df.columns)
print(df.isnull().sum())

# Apply claim extraction
df["extracted_claim"] = df["ai_response"].apply(extract_claim)

# Show results
print(df[["ai_response", "extracted_claim"]])
