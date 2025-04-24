name=input("Enter your name: ")
number=input("Enter your mobile number: ")
email=input("Enter you email id: ")
f=open('D:\\SHYAM\\Python\\Details.vcf','a+')
data=["BEGIN:VCARD\n","VERSION:4.0\n",f"Name: {name}\n",f"MOB: {number}\n",f"EMAIL: {email}\n","END:VCARD\n"]

for lines in data:
    f.write(lines)
f.close()
