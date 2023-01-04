lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = lenght * width * height
volume_liters = volume * 0.001

needed_liters = volume_liters * (1 - (percent / 100))
print(needed_liters)