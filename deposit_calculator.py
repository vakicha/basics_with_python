deposit_sum = float(input())
period_month = int(input())
year_devident = float(input())
mont_devident = deposit_sum * year_devident / 100 / 12

amount = deposit_sum + (period_month * mont_devident)
print(amount)