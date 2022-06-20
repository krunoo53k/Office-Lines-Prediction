filename=input("Enter the dataset name: ")

file = open(filename, "r", encoding="utf8")
output = open("cleaned-office-lines.csv","w")
for line in file:
    line= line.replace("’","'")
    line= line.replace("…","...")
    line= line.replace("“","")
    line= line.replace("”","")
    line= line.replace("–","-")
    output.write(line)