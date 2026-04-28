import spacy

nlp=spacy.load("en_core_web_lg")

text="SQL and Python are two rajvi's strong sense"

doc=nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)