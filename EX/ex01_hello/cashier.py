"""Cha-ching."""
# Asking for user input on a number.
amount = int(input("Enter a sum: "))
# Determining the amount of 50c coins needed
coin50 = amount % 50
sum1 = (amount - coin50) // 50
# Determining the amount of 20c coins needed
coin20 = coin50 % 20
sum2 = (coin50 - coin20) // 20
# Determining the amount of 10c coins needed
coin10 = coin20 % 10
sum3 = (coin20 - coin10) // 10
# Determining the amount of 5c coins needed
coin5 = coin10 % 5
sum4 = (coin10 - coin5) // 5
# Determining the amount of 1c coins needed
coin1 = coin5 % 1
sum5 = (coin5 - coin1) // 1
# Summing up the amount of coins needed
coins = sum1 + sum2 + sum3 + sum4 + sum5
# Printing the amount of coins needed
print(f"Amount of coins needed: {coins}")
