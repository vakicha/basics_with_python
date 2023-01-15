first_part = int(input())
second_part = int(input())
third_part = int(input())

total_time = first_part + second_part + third_part
time_min = total_time // 60
time_sec = total_time % 60

if time_sec < 10:
    print(f"{time_min}:0{time_sec}")
else:
    print(f"{time_min}:{time_sec}")



