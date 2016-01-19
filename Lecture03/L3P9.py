## https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/videosequence:Lecture_3/

## Number guesser

lownum = 0
highnum = 100
def number_guess (lownum, highnum):
	print "Please think of a number between %d and %d!" % (lownum, highnum)
	while True:
		guess = (lownum + highnum) / 2
		print "Is your secret number %d?" % guess
		ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
		if ans != "h" and ans != "l" and ans != "c":
			print "Sorry, I did not understand your input."
		if ans == "h":
			highnum = guess
		if ans == "l":
			lownum = guess
		if ans == "c":
			break
	print "Game over. Your secret number was: %d" % guess
	
number_guess (lownum, highnum)
