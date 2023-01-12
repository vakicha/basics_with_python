kind_of_flower = input()
number_of_flower = int(input())
budget = int(input())
price = 0
final_price = 0
if kind_of_flower == "Roses":
    price = number_of_flower * 5
    if number_of_flower > 80:
        final_price = price - (price*0.1)
    else:
        final_price = price

elif kind_of_flower == "Dahlias":
    price = number_of_flower * 3.80
    if number_of_flower > 90:
       final_price = price - (price * 0.15)
    else:
        final_price = price

elif kind_of_flower == "Tulips":
    price = number_of_flower * 2.80
    if number_of_flower > 80:
        final_price = price - (price * 0.15)
    else:
        final_price = price

elif kind_of_flower == "Narcissus":
    price = number_of_flower * 3
    if number_of_flower < 120:
        final_price = price + (price * 0.15)
    else:
        final_price = price

elif kind_of_flower == "Gladiolus":
    price = number_of_flower * 2.5
    if number_of_flower < 80:
        final_price = price + (price * 0.2)
    else:
        final_price = price
diff = abs(budget - final_price)
if budget >= final_price:
    print(f"Hey, you have a great garden with {number_of_flower} {kind_of_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")



