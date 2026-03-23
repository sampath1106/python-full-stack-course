x = "abc 123| 456 xyz798"
x=x.replace('9','')
numbers = []
i = 0
while i < len(x):
    if x[i].isdigit():
        num = ""
        while i < len(x) and x[i].isdigit():
            num += x[i]
            i += 1
        numbers.append(int(num))
    else:
        i += 1
if numbers:
    print(max(numbers))     
else:
    print("No numbers")
