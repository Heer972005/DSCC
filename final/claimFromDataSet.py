import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Claim extraction function
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


# Load dataset
df = pd.read_excel(r"G:\vs\DSCC\final\hallucination_bias_dataset11.xlsx")

print(df.head())
print(df.columns)
print(df.isnull().sum())

# Apply claim extraction
df["extracted_claim"] = df["ai_response"].apply(extract_claim)

# Show results
print(df[["ai_response", "extracted_claim"]].head(10))
