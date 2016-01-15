## https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Basic_Problem_Set_1/

##COUNTING BOBS
##Assume s is a string of lower case characters

count=0
i=0
while i < (len(s) - 2):
	if s[i:i+3] == "bob":
		count += 1
	i += 1
print "Number of times bob occurs is: %d" % (count)
