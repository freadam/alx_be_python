income = float(input("Enter your monthly income: "))
expense = float(input("Enter your total monthly expenses:"))

monthly_savings = income - expense

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are $ "+ str(monthly_savings))
print("Projected savings after one year, with interest, is: $"+str(int(projected_savings))+".")