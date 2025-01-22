expenses = [10.50, 8, 5, 15, 20, 5, 3]

# Loop approach
total_loop = 0

for x in expenses:
    total_loop += x

print(f"You spent ${total_loop}")

# Function approach

total_function = sum(expenses)

print(f"You spent ${total_function}")
