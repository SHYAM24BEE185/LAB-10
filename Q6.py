with open ('file1.txt','w+') as f1:
    f1.write("I am in file1\nIt is text1\nIt is text2")
    f1.seek(0)
    ch1=f1.readlines()

with open ('file2.txt','w+') as f2:
    f2.write("I am in file2\nIt is text1\nIt is text2")
    f2.seek(0)
    ch2=f2.readlines()

print(ch1,ch2)
with open ('file3.txt','w+') as f3:
    for i,j in zip(ch1,ch2):
        f3.write(i)
        f3.write(j)