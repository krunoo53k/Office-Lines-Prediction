# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:02:03 2022

@author: Bernarda
"""

import spacy
import tkinter as tk

def handle_click(event):
    doc=nlp(quote.get("1.0", tk.END))
    sorted_characters = sorted(doc.cats.items(), key=lambda x: x[1], reverse=True)
    guess.config(text= f'{sorted_characters[0][0]} said this!')
    for i in range(5):
        predictions[i].config(text = f'{sorted_characters[i][0]} {format(sorted_characters[i][1],".2%")}')
        
nlp=spacy.load("en_office_line")

window = tk.Tk()
window.title('Office Line Character Prediction')
window.geometry("600x300")


quote = tk.Text(window, width=50, height=5)
quote.pack()

guess = tk.Label()
guess.pack()

button = tk.Button(
    text="Guess the character",
    width=25,
    height=2
)
button.bind("<Button-1>", handle_click)
button.pack()

predictions = []

for i in range(5):
    label = tk.Label(text=f'{i}')
    label.pack()
    predictions.append(label)

window.mainloop()