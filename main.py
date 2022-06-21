import spacy

nlp=spacy.load("en_office_line")
quote=input("Enter a quote from the Office: ")
doc=nlp(quote)

print(doc.cats)