import shutil,os

if os.path.exists("D:\\Devansh\\Python\\practice"):
    print("Path already exists")
else:
    os.mkdir('D:\\Devansh\\Python\\practice')
    print("Made new directory")

shutil.copyfile('D:\\Devansh\\Python\\File.txt','D:\\Devansh\\Python\\practice\\Copyfile.txt')