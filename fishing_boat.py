budget = int(input())
seson = input()
number_fishman = int(input())
price = 0
final_price = 0
total_final_price = 0
if seson == "Spring":
    price = 3000
    if number_fishman <= 6:
        final_price = price - (price*0.1)
    elif 7 <= number_fishman <= 11:
        final_price = price - (price*0.15)
    elif number_fishman >= 12:
        final_price = price - (price*0.25)

elif seson == "Summer":
    price = 4200
    if number_fishman <= 6:
        final_price = price - (price * 0.1)
    elif 7 <= number_fishman <= 11:
        final_price = price - (price * 0.15)
    elif number_fishman >= 12:
        final_price = price - (price * 0.25)

elif seson == "Autumn":
    price = 4200
    if number_fishman <= 6:
        final_price = price - (price * 0.1)
    elif 7 <= number_fishman <= 11:
        final_price = price - (price * 0.15)
    elif number_fishman >= 12:
        final_price = price - (price * 0.25)

elif seson == "Winter":
    price = 2600
    if number_fishman <= 6:
        final_price = price - (price * 0.1)
    elif 7 <= number_fishman <= 11:
        final_price = price - (price * 0.15)
    elif number_fishman >= 12:
        final_price = price - (price * 0.25)
if seson in ["Spring", "Summer", "Winter" ]:
    if number_fishman % 2 == 0:
        total_final_price = final_price - (final_price*0.05)
    else:
        total_final_price = final_price
else:
    total_final_price = final_price
diff = abs(budget - total_final_price)
if budget >= total_final_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")



