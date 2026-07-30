
print("****************Monthly Expenses Tracker***************")
Expenses=0.0
while True:
    Value=float(input("Enter your Amount"))
    if Value== -1:
       break

    Expenses=Expenses+Value
    print("Total Expenses:", Expenses)
     
