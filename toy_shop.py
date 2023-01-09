
vacancion_price = float(input())
num_puzz = int(input())
num_toy = int(input())
num_bear = int(input())
num_minion = int(input())
num_truck = int(input())

puzz = num_puzz * 2.6
toy = num_toy * 3
bear = num_bear * 4.1
minion = num_minion * 8.2
truck = num_truck * 2

total_number_sels = num_truck + num_toy + num_minion + num_bear + num_puzz
total_price = puzz + toy + bear + minion + truck
if total_number_sels >= 50:
    total_price -= total_price * 0.25
final_price = total_price - (total_price * 0.1)
diff = abs(final_price - vacancion_price)
if final_price >= vacancion_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")