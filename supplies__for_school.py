pen_number = int(input())
marker_number = int(input())
chem_lt = int(input())
discount_percent = int(input())

sum_pen = pen_number * 5.8
sum_maker = marker_number * 7.2
sum_chem = chem_lt * 1.2

sum_all_prod = sum_pen + sum_maker + sum_chem

total_sum = sum_all_prod - (sum_all_prod * discount_percent / 100)

print(total_sum)


