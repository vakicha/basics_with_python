import math

expected_numbers_of_procesors = int(input())
number_of_workers = int(input())
work_days = int(input())
total_hours_of_work = number_of_workers * work_days * 8
sum_of_produced_procesors = math.floor(total_hours_of_work / 3)
if sum_of_produced_procesors >= expected_numbers_of_procesors:
    print(f"Profit: -> {((sum_of_produced_procesors - expected_numbers_of_procesors) * 110.1):.2f} BGN")
else:
    print(f"Losses: -> {((expected_numbers_of_procesors - sum_of_produced_procesors) * 110.1):.2f} BGN")
