import spacy

nlp=spacy.load("en_office_prediction")
nlp2=spacy.load("en_office_prediction-0.0.2")
doc=nlp("That's what she said!")
doc2=nlp2("That's what she said!")

print(doc.cats)
print(doc2.cats)