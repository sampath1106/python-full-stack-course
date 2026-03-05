file=open("details.csv","w")
file.close()
import os
def Write():
    file_name=input("Enter file name:")
    if os.path.exists(file_name):
        with open(file_name,"w") as file:
            file.write("name,age,marks\n")
            name=input("Enter name :")
            age=int(input("enter age:"))
            marks=int(input("enter marks:"))
            file.write(f"{name},{age},{marks}\n")
            print("Completed")
    else:
        print("File not found")
        
def Update():
    file_name=input("Enter file name:")
    if os.path.exists(file_name):
        with open(file_name,"a") as file:
            name=input("Enter name: ")
        with open (file_name,"r+") as file:
            data=file.readlines()
            for i in data:
                i=i.strip().split(",")
                if i[0]==name:
                    print("Already exist")
                    break
            else:
                age=int(input("Enter age "))
                marks=int(input("Enter marks "))
                file.write(f"{name},{age},{marks}\n")
                print("Completed")
    else:
        print("File not found")
        
while True:
    print("1.Write\n" "2.Update")
    n=int(input("Enter operation : "))
    if n==1:
        Write()
    elif n==2:
        Update()
