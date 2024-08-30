name = input("Please Enter Your name ")

reversed_names = ""
for i in range(len(name) -1,-1,-1):
    reversed_names += name[i]
    
print(reversed_names)    