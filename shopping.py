budget = float(input())
number_videocards = int(input())
number_processors = int(input())
number_ram = int(input())
videocard_price = 250 * number_videocards
processors_price = (videocard_price * 0.35) * number_processors
ram_price = (videocard_price * 0.1) * number_ram

total_price = videocard_price + processors_price + ram_price

if number_videocards > number_processors:
    total_price = total_price - (total_price * 0.15)
diff = abs( total_price - budget)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")







