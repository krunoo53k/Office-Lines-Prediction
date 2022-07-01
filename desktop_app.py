import tkinter as tk
import requests

api_url="http://localhost:5000/character"

def handle_click(event):
    guess.config(text= f'Loading request...')
    user_input={"line":quote.get("1.0", tk.END)}
    api_output=requests.get(api_url,json=user_input)
    guess.config(text= f'{api_output.text} said this!')
        

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


window.mainloop()