with open ("first.txt","w+") as d:
    d.write("SHYAM is a person\nHe is also a small child")

with open ("first.txt","r") as d:
    ch=d.readlines()
    print(ch)

ch1=[]

for i in ch:
    if " a " in i or " the " in i or " an " in i:
        i=i.replace(" a "," ").replace(" an "," ").replace(" the "," ")
        ch1.append(i)

with open ("first.txt","w") as d:
    for i in ch1:
        d.write(i)

