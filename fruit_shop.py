name_of_fruit = input()
name_of_day = input()
quantity = float(input())
price = 0
flag = True
if name_of_day in ["Monday" , "Tuesday" ,"Wednesday" , "Thursday" , "Friday" ]:
    if  name_of_fruit == "banana":
        price = quantity * 2.50
    elif  name_of_fruit == "apple":
        price = quantity * 1.20
    elif name_of_fruit == "orange":
        price = quantity * 0.85
    elif name_of_fruit == "grapefruit":
        price = quantity * 1.45
    elif name_of_fruit =="kiwi":
        price = quantity * 2.70
    elif name_of_fruit == "pineapple":
        price = quantity * 5.50
    elif name_of_fruit == "grapes":
        price = quantity * 3.85
    else:
        flag = False
elif name_of_day in ["Saturday" , "Sunday"]:
    if  name_of_fruit == "banana":
        price = quantity * 2.70
    elif  name_of_fruit == "apple":
        price = quantity * 1.25
    elif name_of_fruit == "orange":
        price = quantity * 0.90
    elif name_of_fruit == "grapefruit":
        price = quantity * 1.60
    elif name_of_fruit =="kiwi":
        price = quantity * 3.00
    elif name_of_fruit == "pineapple":
        price = quantity * 5.60
    elif name_of_fruit == "grapes":
        price = quantity * 4.20
    else:
        flag = False
else:
    flag = False
if flag == True:
    print(f"{price:.2f}")
else:
    print("error")

