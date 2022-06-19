import spacy

nlp=spacy.load("en_office_prediction")

doc=nlp("[singing] Shall I play for you? Pa rum pump um pum [Imitates heavy drumming] I have no gifts for you. Pa rum pump um pum [Imitates heavy drumming]")

print(doc.cats)