
total_sheet_number = int(input())
per_hour_sheet_number = int(input())
days_number = int(input())
hours_per_day = (total_sheet_number // per_hour_sheet_number)
need_time_per_day = hours_per_day / days_number


print(need_time_per_day)


