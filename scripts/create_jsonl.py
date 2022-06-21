import pandas as pd

characters = ["Michael", "Jim", "Dwight", "Angela", "Kelly"]

for character in characters:

    df = pd.read_csv(f'character_lines_cleaned/office-{character}-lines-cleaned.csv')
    df.drop(df.columns[0], axis=1, inplace=True)
    df.drop(columns=['Season'], axis=1, inplace=True)
    df.drop(columns=['Episode_Number'], axis=1, inplace=True)
    
    
    df=df.assign(Michael=0.0,Jim=0.0,Dwight=0.0,Angela=0.0,Kelly=0.0)
    
    df.drop(df.columns[0], axis=1, inplace=True)
    
    names=df['Character'].unique()
    for name in names:
        df.loc[df.Character==name,name]=1.0
    
    df.drop(['Character'], axis=1, inplace=True)
    df.insert(1, 'cats',"")
    print(df)
    
    f=open(f'jsonl/{character}-lines.jsonl',"w")
    print(df.to_json(orient='records', lines=True),file=f, flush=False)