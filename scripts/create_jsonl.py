import pandas as pd

df = pd.read_csv("final-5only.csv")

df=df.assign(Michael=0.0,Dwight=0.0,Jim=0.0,Pam=0.0)

df.drop(df.columns[0], axis=1, inplace=True)

df.loc[df.Character=="Michael",'Michael']=1.0
df.loc[df.Character=="Dwight",'Dwight']=1.0
df.loc[df.Character=="Jim",'Jim']=1.0
df.loc[df.Character=="Pam",'Pam']=1.0
df.drop(['Character'], axis=1, inplace=True)
df.insert(1, 'cats',"")
print(df)

f=open('lines.jsonl',"w")
print(df.to_json(orient='records', lines=True),file=f, flush=False)