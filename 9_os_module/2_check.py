import os

print (os.getcwd()) #show us the root directory

print("*******************")

print(os.path.abspath(__file__)) #get absolute path of file


print("*******************")

print(os.path.dirname(os.path.abspath(__file__))) #get the current directory

print("*******************")

print(os.listdir())

print("*******************")

# for i in os.listdir():
#     if os.path.isfile(i):
#         print(f"{i} is a file")
#     elif os.path.isdir(i):
#         print(f"{i} is a dir")

print("*******************")

print(os.listdir(os.path.dirname(os.path.abspath(__file__))))

print("*******************")

print(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Data")))

print("*******************")
print("*******************")

last_load = '2026-01-14'

for i in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Data")):
    if i.split(".")[0]>last_load:
        print(f"Processing {i} new file")