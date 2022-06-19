import pandas as pd

df = pd.read_csv("final-5only.csv")


f=open('lines.jsonl',"w")
print(df.to_json(orient='records', lines=True),file=f, flush=False)