import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities_relations(text):
    doc = nlp(text)

    entities = []
    relations = []

    for token in doc:
        # Entities: nouns and proper nouns
        if token.pos_ in ["NOUN", "PROPN"]:
            entities.append(token.text)

        # Relations: main verbs
        if token.pos_ == "VERB":
            relations.append(token.lemma_)

    return entities, relations


# Test
sample_claim = "Sydney is the capital of Australia"
ents, rels = extract_entities_relations(sample_claim)

print("Claim:", sample_claim)
print("Entities:", ents)
print("Relations:", rels)
