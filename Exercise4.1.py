print("********** Order Tracking Simulation System ***********")

status =  input("Enter order Status:").lower()

if status == " shipped ":
    print(" Your Order is shipped and is on the way.")

elif status == "delivered":
    print(" Your Order is delivered Successfull.")

elif status == "pending":
    print(" Your Order is currently pending and will be processed soon.")

else:
    print("invalid status.")
    print(" Enter shipped , delivered or pending.")
