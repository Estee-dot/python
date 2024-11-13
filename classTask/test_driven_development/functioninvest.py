def get_investment(investment_amount, monthly_interest_rate, number_of_months):
	future_investment = investment_amount * (1+monthly_interest_rate)** number_of_months
	return round(future_investment,2)

	