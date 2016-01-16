##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Basic_Problem_Set_1/

##PROBLEM 3: COUNTING AND GROUPING
##Write a function called item_order that takes as input a string named order.

def item_order (order):
	salad_count=0
	hamburger_count=0
	water_count=0
	order_list=order.split()
	for item in order_list:
		if item=="salad":
			salad_count+=1
		if item=="hamburger":
			hamburger_count+=1
		if item=="water":
			water_count+=1
	return "salad:%d hamburger:%d water:%d" % (salad_count, hamburger_count, water_count)
