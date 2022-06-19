import spacy

nlp=spacy.load("en_office_prediction")
nlp2=spacy.load("en_office_prediction-0.0.2")
quote=input("Enter a quote from the Office: ")
doc=nlp(quote)
doc2=nlp2(quote)

print(doc.cats)
print(doc2.cats)