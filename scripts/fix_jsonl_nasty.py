import re

f=open("lines.jsonl")

output = open("data.jsonl","x")
for line in f:
    line= line.replace('"cats":"",','"cats":{')
    line= line.replace("}","}}")
    output.write(line)

