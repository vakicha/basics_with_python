number_chiken = int(input())
number_fish = int(input())
number_vege = int(input())

price_chiken = number_chiken * 10.35
price_fish = number_fish * 12.4
price_vege = number_vege * 8.15

price_all_menus = price_chiken + price_fish + price_vege
desert = price_all_menus * 0.2
delivery = 2.5
total_price = price_all_menus + desert + delivery
print(total_price)

