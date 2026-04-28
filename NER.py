import spacy

nlp=spacy.load("en_core_web_lg")

text="My name is rajvi dave and i am queen and winner of this world"

doc=nlp(text)

print("Token\t\tPOS Tag")
print("-----------------------")
for token in doc:
    print(f"{token.text}\t\t{token.pos_}")