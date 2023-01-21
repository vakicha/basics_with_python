city = input()
quantity_sels = float(input())
comission = 0


if city == "Sofia":
    if 0 <= quantity_sels <= 500:
        comission = quantity_sels * 0.05
        print(f"{comission:.2f}")
    elif 500 < quantity_sels <= 1000:
        comission = quantity_sels * 0.07
        print(f"{comission:.2f}")
    elif 1000 < quantity_sels <= 10000:
        comission = quantity_sels * 0.08
        print(f"{comission:.2f}")
    elif quantity_sels > 10000:
        comission = quantity_sels * 0.12
        print(f"{comission:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= quantity_sels <= 500:
        comission = quantity_sels * 0.045
        print(f"{comission:.2f}")
    elif 500 < quantity_sels <= 1000:
        comission = quantity_sels * 0.075
        print(f"{comission:.2f}")
    elif 1000 < quantity_sels <= 10000:
        comission = quantity_sels * 0.1
        print(f"{comission:.2f}")
    elif quantity_sels > 10000:
        comission = quantity_sels * 0.13
        print(f"{comission:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= quantity_sels <= 500:
        comission = quantity_sels * 0.055
        print(f"{comission:.2f}")
    elif 500 < quantity_sels <= 1000:
        comission = quantity_sels * 0.08
        print(f"{comission:.2f}")
    elif 1000 < quantity_sels <= 10000:
        comission = quantity_sels * 0.12
        print(f"{comission:.2f}")
    elif quantity_sels > 10000:
        comission = quantity_sels * 0.145
        print(f"{comission:.2f}")
    else:
        print("error")
else:
    print("error")

