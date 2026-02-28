def tree(n):
    if n<=1:
        return n
    return tree (n-1)+tree (n-2)
num=int(input("enter a number :"))
print(tree(num))
