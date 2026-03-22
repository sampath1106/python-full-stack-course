amount=int(input("enter a numbeer:"))
if amount<=1000:
    dicount=0.05
elif amount<=2000:
    discount=0.10
elif amount<=3000:
    discount=0.20
else:
    null
discount_amount=amount*discount
final_amount= amount-discount_amount

print("discount_amount:",discount_amount)
print("total_amount:",final_amount)
