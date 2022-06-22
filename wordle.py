import string
check = ["A", "R", "E"]
tmp = []
garb = []

with open('text.txt','r') as f:
    mylist = list(f)
    for line in mylist:
        text = [word.strip(string.punctuation) for word in line.split()]
for each in text:
    tmp.append(list(each))

for each in tmp:
    if "N" in each and "I" in each and "A" not in each and "R" not in each and "E" not in each and "O" not in each and "G" not in each and "U" not in each and "M" not in each and "L" not in each and "T" not in each:
        garb.append(each)


print(garb)

