f=open("D:\\SHYAM\\Python\\First_Csv.csv")
data=f.readlines()
all_lines=[lines.strip().split(',') for lines in data]
empty_dict={}
columns=len(all_lines[0])
for i in range(columns):
    empty_dict[all_lines[0][i]]=[lines[i] for lines in all_lines[1:]]
f.close()
print(empty_dict)
