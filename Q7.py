import json

emp_lst=[]

emp_code=input("Enter your employee code[Press enter to exit]: ")
while emp_code:
    emp_name=input("Enter your name: ")
    join_date=input("Enter the date of joining[DD-MM-YY]: ")
    salary=input("Enter your salary: ")
    emp_data={"emp_code":emp_code,"emp_name":emp_name,"join_date":join_date,"salary":salary}
    emp_lst.append(emp_data)
    emp_code=input("Enter your employee code[Press enter to exit]: ")

with open('empdata.txt','w') as f:
    json.dump(emp_lst,f)
        

with open('empdata.txt', 'r') as f:
    data_list=json.load(f)
    print("\nEmployee data:\n")
    for i in data_list:
        print(f"Employee code: {i['emp_code']}\nName: {i["emp_name"]}\nDate of joining: {i["join_date"]}\nSalary: {i['salary']}\n")
