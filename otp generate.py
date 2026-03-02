import random
otp=""
for i in range(4):
    digit=random.randint(1,9)
    otp+=otp+str(digit)
print("your otp:",otp)
