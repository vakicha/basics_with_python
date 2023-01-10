name_of_month = input()
number_of_days = int(input())
price_studio = 0
price_flat = 0
if name_of_month in ["May", "October"]:
    price_studio = number_of_days * 50
    price_flat = number_of_days * 65
    if 14 >= number_of_days > 7:
        price_studio = price_studio * 0.95
    elif number_of_days > 14:
        price_studio = price_studio * 0.70

elif name_of_month in ["June", "September"]:
    price_studio = number_of_days * 75.20
    price_flat = number_of_days * 68.70
    if number_of_days > 14:
        price_studio = price_studio * 0.8

elif name_of_month in ["July", "August"]:
    price_studio = number_of_days * 76
    price_flat = number_of_days * 77
if number_of_days > 14:
    price_flat = price_flat * 0.9
print(f"Apartment: {price_flat:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
