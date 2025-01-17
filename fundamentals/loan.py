money_owed = float(input(f"How much money in dollars do you owe?\n"))
apr = float(input(f"What annual percentage rate does the loan have?\n"))
payment = float(input(f"How much in dollars will you pay off each month?\n"))
months = int(input(f"How many results should factor into the calculation?\n"))

monthly_rate = apr / 100 / 12

for i in range(months):
    interest_paid = money_owed * monthly_rate

    money_owed = money_owed + interest_paid

    if money_owed - payment < 0:
        print(f"The last payment is {money_owed}.")
        print(f"You paid off the loan in {i + 1} months.")
        break

    money_owed = money_owed - payment

    print(f"Paid {payment}, of which {interest_paid} went toward interest.", end=" ")
    print(f"Now you owe {money_owed}.")
