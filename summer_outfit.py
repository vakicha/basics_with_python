degreese = int(input())
time = input()
outfit = 0
shoes = 0
if time == "Morning":
    if 10 <= degreese <= 18:
        shoes = "Sneakers"
        outfit = "Sweatshirt"
    elif 18 < degreese <= 24:
        shoes = "Moccasins"
        outfit = "Shirt"
    elif 25 <= degreese:
        shoes = "Sandals"
        outfit = "T-Shirt"

elif time == "Afternoon":
    if 10 <= degreese <= 18:
        shoes = "Moccasins"
        outfit = "Shirt"
    elif 18 < degreese <= 24:
        shoes = "Sandals"
        outfit = "T-Shirt"
    elif 25 <= degreese:
        shoes = "Barefoot"
        outfit = "Swim Suit"

elif time == "Evening":
    if 10 <= degreese <= 18:
        shoes = "Moccasins"
        outfit = "Shirt"
    elif 18 < degreese <= 24:
        shoes = "Moccasins"
        outfit = "Shirt"
    elif 25 <= degreese:
        shoes = "Moccasins"
        outfit = "Shirt"
print(f"It's {degreese} degrees, get your {outfit} and {shoes}.")



