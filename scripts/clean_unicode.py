characters = ["Michael", "Jim", "Dwight", "Angela", "Kelly"]

for character in characters:
    filename = f'character_lines/office-{character}-lines.csv'
    file = open(filename, "r", encoding="utf8")
    output = open(f'character_lines_cleaned/office-{character}-lines-cleaned.csv',"w")
    for line in file:
        line= line.replace("’","'")
        line= line.replace("…","...")
        line= line.replace("“","")
        line= line.replace("”","")
        line= line.replace("–","-")
        output.write(line)