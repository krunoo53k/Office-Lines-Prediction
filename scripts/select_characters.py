import pandas as pd

filename = input("Insert the dataset name: ")
df = pd.read_csv(filename)

characters = ["Michael", "Jim", "Dwight", "Angela", "Kelly"]

for character in characters: 
    df = pd.read_csv(filename)
    df = df.loc[(df['Character']==character)]
    df.to_csv(f'character_lines/office-{character}-lines.csv')
