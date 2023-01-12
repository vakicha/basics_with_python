number_1 = int(input())
number_2 = int(input())
operator = input()
summ = 0
if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
      sum = number_1 + number_2
    elif operator == "-":
      sum = number_1 - number_2
    elif operator == "*":
        sum = number_1 * number_2
    if sum % 2 == 0:
        print(f"{number_1} {operator} {number_2} = {sum} - even")
    else:
        print(f"{number_1} {operator} {number_2} = {sum} - odd")

elif operator == "/" and number_2 != 0:
    sum = number_1 / number_2
    print(f"{number_1} {operator} {number_2} = {sum:.2f}")

elif operator == "%" and number_2 != 0:
    sum = number_1 % number_2
    print(f"{number_1} {operator} {number_2} = {sum}")
if number_2 == 0 and (operator == "/" or operator == "%"):
    print(f"Cannot divide {number_1} by zero")
