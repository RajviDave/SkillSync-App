import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load("en_core_web_sm")

ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    {"label": "SKILL", "pattern": "Python"},
    {"label": "SKILL", "pattern": "Machine Learning"},
    {"label": "SKILL", "pattern": "React"},
]

ruler.add_patterns(patterns)

doc = nlp("Skilled in Python and Machine Learning")

for ent in doc.ents:
    print(ent.text, ent.label_)