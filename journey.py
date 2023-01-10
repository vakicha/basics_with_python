budget = float(input())
season = input()
destination = ""
type_of_vacantion = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
    else:
        price = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
    else:
        price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    price = budget * 0.9
if season == "winter" or destination == "Europe":
    type_of_vacantion = "Hotel"
else:
    type_of_vacantion = "Camp"
diff = abs(budget - price)
print(f"Somewhere in {destination}")
print(f"{type_of_vacantion} - {price:.2f}")


