monthly_income = int (input('Enter your monthly income:'))
total_monthly_expenses = int(input('Enter your total monthly expenses'))
monthly_savings = monthly_income - total_monthly_expenses
interest_rate = 0.05


projected_annual_savings = (monthly_savings * 12 + (monthly_savings * 12 * interest_rate))
print(f'Your monthly savings are ${monthly_savings}')
print(f'Projected savings after one year, with interest is: ${projected_annual_savings}')