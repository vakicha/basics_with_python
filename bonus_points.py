string = int(input())
bonus = 0
if string <= 100:
    bonus = 5
elif string < 1000:
    bonus += string * 0.2
else:
    bonus += string * 0.1
if string % 2 == 0:
    bonus += 1
if string % 10 == 5:
    bonus += 2
print(bonus)
print(string + bonus)