nylon = int(input())
painte = int(input())
thinner = int(input())
hours_of_work = int(input())
sum_nylon = (nylon + 2) * 1.5
sum_painte = (painte + (painte * 0.1)) * 14.5
sum_thinner = thinner * 5
sum_bags = 0.4
all_products_sum = sum_bags + sum_thinner + sum_painte + sum_nylon
sum_workers = (all_products_sum * 0.3 ) * hours_of_work
total_sum = all_products_sum + sum_workers

print(total_sum)



