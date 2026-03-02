num=int(input("enter a number :"))
sum_of_divisiors=0
for i in range(1,num):
    if num%i==0:
        sum_of_divisiors+=i
if sum_of_divisiors==num:
        print(num,"perfrct number: ")
else:
    print("not perfrct number :")
    
