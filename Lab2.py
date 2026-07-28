print("*****************Grossary shop billing calculator***************")
rice_qty = float(input("Enter the quantity of rice(in kg):"))
rice_price_per_kg= 60
rice_total = rice_qty*rice_price_per_kg

sugar_qty = float(input("Enter the quantity of sugar(in kg):"))
sugar_price_per_kg= 80
sugar_total = sugar_qty*sugar_price_per_kg

salt_qty = float(input("Enter the quantity of salt(in kg):"))
salt_price_per_kg= 40
salt_total = salt_qty*salt_price_per_kg

oil_qty = float(input("Enter the quantity of oil(in kg):"))
oil_price_per_kg= 100
oil_total = oil_qty*oil_price_per_kg

print("*************Bill Detail******************")

print("rice:",rice_total)
print("sugar:",sugar_total)
print("salt:",salt_total)
print("oil:",oil_total)

Total_Bill = rice_total + sugar_total + salt_total+ oil_total
print("Total Bill:",Total_Bill)

Discount=0

if Total_Bill >= 2000:
   Discount=Total_Bill*0.1
   print("Discount:",Discount)

elif Total_Bill>=1000:
   Discount=Total_Bill*0.05
   print("Discount:",Discount)
   
else:
   print("no Discount")

Final_Bill = Total_Bill - Discount
print("Final_Bill:", Final_Bill)