### https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Problem_Set_2/

### PROBLEM 2: PAYING DEBT OFF IN A YEAR

months = 12
def calculate_monthly_payments_payoff (balance, annualInterestRate, months):
	'''
	balance - ammount of loan
	annualInterestRate - annual % that bank takes from balance every month
	months - period that require to calculate
	Calculates the minimum fixed monthly payment needed in order pay off 
	a credit card balance within %months%.
	'''
	monthlyInterestRate = annualInterestRate / 12
	minPayment = 0
	unpaidBalance = balance
	while True:
		minPayment += 10
		unpaidBalance = balance
		for month in xrange(months):
			unpaidBalance = (unpaidBalance - minPayment) * (1 + monthlyInterestRate)
		if unpaidBalance <= 0:
			break
	print "Lowest Payment: %d" % minPayment

calculate_monthly_payments_payoff (balance, annualInterestRate, months)
