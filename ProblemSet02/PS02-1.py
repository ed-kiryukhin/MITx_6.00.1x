## https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Problem_Set_2/

## PROBLEM 1: PAYING THE MINIMUM

def calculate_monthly_payments (balance, annualInterestRate, monthlyPaymentRate, months):
	'''
	balance - ammount of loan
	annualInterestRate - annual % that bank takes from balance every month
	monthlyPaymentRate - min % of balance that bank claim to pay
	months - period that require to calculate
	Calculates the credit card balance after %months% if a person only pays 
	the minimum monthly payment required by the credit card company each month.
	'''
	monthlyInterestRate = annualInterestRate / 12
	totalPaid = 0
	for month in xrange(months):
		minMonthlyPayment = balance * monthlyPaymentRate
		totalPaid += minMonthlyPayment
		unpaidBalance = balance - minMonthlyPayment
		balance = unpaidBalance * (1 + monthlyInterestRate)
	
		print "Month: %d" % (month+1)
		print "Minimum montly payment: %.2f" % minMonthlyPayment
		print "Remaining balance: %.2f" % balance
	
	print "Total paid: %.2f" % totalPaid
	print "Remaining balance: %.2f" % balance

months = 12	
calculate_monthly_payments (balance, annualInterestRate, monthlyPaymentRate, months)
