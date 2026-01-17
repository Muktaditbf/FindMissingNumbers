# 1. The list with one number missing
numbers = [1, 2, 4, 5]

# 2. Find the biggest number (N)
n = numbers[-1] # This gets '5' (the last number)

# 3. Calculate expected sum (1 + 2 + 3 + 4 + 5)
# range(1, n+1) creates numbers from 1 to 5
expected_sum = sum(range(1, n + 1))

# 4. Calculate actual sum (1 + 2 + 4 + 5)
actual_sum = sum(numbers)

# 5. The difference is the missing number
missing_number = expected_sum - actual_sum

print("The missing number is:", missing_number)