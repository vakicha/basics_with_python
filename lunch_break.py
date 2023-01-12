from math import ceil

name_of_movie = input()
time_movie = int(input())
time_break = int(input())
time_lunch = time_break / 8
relax_time = time_break / 4
total_break = time_lunch + relax_time + time_movie

diff = abs(time_break - total_break)
rouded_diff = ceil(diff)

if time_break >= total_break:
    print(f"You have enough time to watch {name_of_movie} and left with {rouded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {rouded_diff} more minutes.")




