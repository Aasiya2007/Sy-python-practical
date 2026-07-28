print("****************College Admision Eligiblity***************")

num_age = int(input("Enter your age:"))
num_mark = int(input("Enter your mark:"))

if num_age>17 and num_age<25:
    print("you are eligible for Admision")

    if num_mark>60:
       if num_mark>80:
          print("you are eligible for AIML department")

       elif num_mark<80:
          print("you are eligible for CSE department")

    elif num_mark<70:
       print("you are eligible for genral")

else:
      print("you are not eligible for admision")
