input_hours = int(input())
input_minets = int(input())

total_input_minets = (input_hours * 60) + input_minets + 15
output_hour = total_input_minets // 60
output_minets = total_input_minets % 60
if output_hour == 24:
    output_hour = 0
print(f"{output_hour}:{output_minets:02d}")