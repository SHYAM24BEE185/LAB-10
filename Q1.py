f=open("First_Csv.csv",'w+')
roll_num=input("Enter roll number[Press enter to exit]: ")
f.write(f"Roll number,Name,Computer,Mathematics,Chemistry\n")
while roll_num:
    name=input("Enter your name: ")
    comp,maths,chem=input("Enter the marks by keeping space: ").split()
    f.write(f"{roll_num},{name},{comp},{maths},{chem}\n")
    roll_num=input("Enter roll number[Press enter to exit]: ")
f.close()