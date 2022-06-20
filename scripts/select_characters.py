import pandas as pd
import utils

filename = input("Insert the dataset name: ")
df = pd.read_csv(filename)

df=df.loc[(df['Character']=="Michael") | (df['Character']=="Jim") | (df['Character']=="Dwight") | (df['Character']=="Pam") | (df['Character']=="Phyllis") 
| (df['Character']=="Angela") | (df['Character']=="Stanley") | (df['Character']=="Jan") | (df['Character']=="Creed") | (df['Character']=="Ryan") | (df['Character']=="Kelly") | (df['Character']=="Oscar") | (df['Character']=="Kevin") | (df['Character']=="Darryl") | (df['Character']=="Andy") | (df['Character']=="Toby") | (df['Character']=="Erin") | (df['Character']=="Gabe")]

df.to_csv("cleaned-office-lines-bea.csv")