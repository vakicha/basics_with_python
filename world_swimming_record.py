wolrd_record = float(input())
distance_m = float(input())
time_swim_1_m = float(input())
deley = (distance_m // 15) * 12.5

ivans_time = (distance_m * time_swim_1_m) + deley
diff = abs(wolrd_record - ivans_time)

if ivans_time >= wolrd_record:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {ivans_time:.2f} seconds.")
