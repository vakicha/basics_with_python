input_hours = int(input())
input_mins = int(input())

total_mins = (input_hours * 60) + input_mins + 15
hours = total_mins // 60
mins = total_mins % 60
if hours == 24:
    hours = 0
if mins < 10:
    mins = (f"0{mins}")
print(f"{hours}:{mins}")






