import csv
redirs=[]
with open("redir.csv") as f:
    lines = csv.reader(f)
    for line in lines:
        redirs.append(line)


for urls in redirs[1:]:
    urls[1]=f"https://nye.obos.no{urls[1]}"


with open("redir2.csv","w") as f:
    write = csv.writer(f,delimiter="|")
    for line in redirs:
        write.writerow(line)