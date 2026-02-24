w=input("enter a string")
v=0
c=0
for i in w:
    if i.isalpha():
        if i.lower()in'aeiou':
            v+=1
        else:
            c+1
print("number of vowels",v)
print("number of consunents",c)
    
