n=int(input())
arr=list(map(int,input("enter a nnumber:").split()))
j=0
for i in  range(n):
    if arr[i]!=0:
        if arr[i]!=j:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
print(*arr)
