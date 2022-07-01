from flask import Flask, request, jsonify
import spacy

nlp=spacy.load("en_office_line")


app = Flask(__name__)

@app.get("/character")
def get_character():
    if request.is_json:
        input_json=request.get_json()
        line=input_json["line"]
        doc=nlp(line)
        predicted_character=max(doc.cats,key=doc.cats.get)
        return predicted_character,201
    return {"error": "Request must be JSON"}, 415