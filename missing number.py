
n=int(input("one element:"))
arr=list(map(int,input("elements:").split()))
execpted_sum=n*(n+1)//2
actual_sum=sum(arr)
missing_number=execpted_sum-actual_sum
print("missing number:",missing_number)
