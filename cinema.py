type_proj = input()
r = float(input())
c = float(input())
sum = 0
if type_proj == "Premiere":
    sum = c * r * 12
elif type_proj == "Normal":
    sum = c * r * 7.5
elif type_proj == "Discount":
    sum = c * r * 5
print(f"{sum:.2f} leva")


