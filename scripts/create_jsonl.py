import pandas as pd

df = pd.read_csv(input("Insert the file name: "))

df=df.assign(Michael=0.0,Dwight=0.0,Jim=0.0,Pam=0.0)

df.drop(df.columns[0], axis=1, inplace=True)

names=df['Character'].unique()
for name in names:
    df.loc[df.Character==name,name]=1.0

df.drop(['Character'], axis=1, inplace=True)
df.insert(1, 'cats',"")
print(df)

f=open('lines.jsonl',"w")
print(df.to_json(orient='records', lines=True),file=f, flush=False)