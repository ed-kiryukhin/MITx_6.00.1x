## https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Basic_Problem_Set_1/

## COUNTING VOWELS
## Assume s is a string of lower case characters

count=0
for letter in s:
	if letter in "aeiou":
		count += 1
print "Number of vowels: %d" % (count)
