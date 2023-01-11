budget = float(input())
number_personal = int(input())
price_for_dress_personal = float(input())
decor = budget * 0.1
total_price_for_personel = number_personal * price_for_dress_personal
if number_personal > 150:
    total_price_for_personel = total_price_for_personel - (total_price_for_personel * 0.1)
final_sum = total_price_for_personel + decor
diff = abs(final_sum - budget)

if final_sum <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")



