x=["python","java","codegnan","gnan"]
print(list(map(lambda x:x[0].upper(),x)))
print(list(map(lambda x:x[0].upper()+x[1:],x)))
print(list(map(lambda x:len(x),x)))
print(list(map(lambda x:x if len(x)>4 else "false",x)))
print(list(map(lambda x:x if "a" in x else "false",x)))

x=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x%2!=0,x)))
print(list(filter(lambda x:x%2==0,x)))

n=["akhil","aravind","jeswanth","prakesh"]
print(list(filter(lambda n:n.startswith("a"),n)))

n=["abc@gmail.com","xyz@yahoo.com","mms@gmail.com"]
print(list(filter(lambda n:n.endswith("@gmail.com"),n)))

n=  "abc123"
print("".join(list(filter(lambda n:n.isalpha(),n))))


