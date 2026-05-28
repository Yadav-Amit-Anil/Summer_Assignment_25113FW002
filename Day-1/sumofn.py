n = int(input("Enter a number: "))

# Formula method
sum_formula = n * (n + 1) // 2
print("Sum using formula:", sum_formula)

# Loop method
sum_loop = 0
for i in range(1, n + 1):
    sum_loop += i
print("Sum using loop:", sum_loop)