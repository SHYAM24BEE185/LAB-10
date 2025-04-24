import shutil,os

if os.path.exists("D:\\SHYAM\\Python\\practice"):
    print("Path already exists")
else:
    os.mkdir('D:\\SHYAM\\Python\\practice')
    print("Made new directory")

shutil.copyfile('D:\\SHYAM\\Python\\File.txt','D:\\SHYAM\\Python\\practice\\Copyfile.txt')
