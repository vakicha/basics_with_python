vacantion_price = float(input())
number_puzzels = int(input())
number_toys = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
total_number = number_puzzels + number_toys + number_bears + number_minions + number_trucks
sum_puzzels = number_puzzels * 2.6
sum_toys = number_toys * 3
sum_bears = number_bears * 4.1
sum_minions = number_minions * 8.2
sum_trucks = number_trucks * 2

total_sum = sum_puzzels + sum_toys + sum_bears + sum_minions + sum_trucks
if total_number >= 50:
    total_sum = total_sum - (total_sum * 0.25)
final_sum = total_sum - (total_sum * 0.1)
diff = abs(vacantion_price - final_sum)
if final_sum >= vacantion_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")





