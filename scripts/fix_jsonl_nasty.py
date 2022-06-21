import re

characters = ["Michael", "Jim", "Dwight", "Angela", "Kelly"]

for character in characters:
    
    f=open(f'jsonl/{character}-lines.jsonl')
    
    output = open(f'data/{character}-lines.jsonl',"x")
    for line in f:
        line= line.replace('"cats":"",','"cats":{')
        line= line.replace("}","}}")
        
        line = line.replace("\" ", "\"")
        line = line.replace("\" ", "\"")
        
        line = line.replace(" \"", "\"")
        line = line.replace(" \"", "\"")
        line = line.replace(" \"", "\"")
        output.write(line)

