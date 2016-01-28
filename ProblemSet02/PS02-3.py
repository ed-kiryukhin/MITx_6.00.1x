## https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Problem_Set_2/

## PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER

months = 12
def calculate_monthly_payments_payoff_bisect (balance, annualInterestRate, months):
	'''
	balance - ammount of loan
	annualInterestRate - annual % that bank takes from balance every month
	months - period that require to calculate
	Calculates the minimum fixed monthly payment needed in order pay off 
	a credit card balance within %months%. Bisection search used.
	'''
	monthlyInterestRate = annualInterestRate / 12
	epsilon = 0.001
	low = balance / months
	high = ( balance * (1 + monthlyInterestRate) ** months ) / months
	unpaidBalance = balance
	payment = ( low + high ) / 2
	while True:
		unpaidBalance = balance
		payment = ( low + high ) / 2
		for month in xrange (months):
			unpaidBalance = ( unpaidBalance - payment ) * ( 1 + monthlyInterestRate )
		if abs(unpaidBalance) < epsilon:
			break
		elif unpaidBalance > 0:
			low = payment
		elif unpaidBalance < 0:
			high = payment
	print "Lowest Payment: %.2f" % payment
	
calculate_monthly_payments_payoff_bisect (balance, annualInterestRate, months)
