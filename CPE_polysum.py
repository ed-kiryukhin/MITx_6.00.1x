##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/2e11590fc59d4bc99f4ad988747eec51/

##CODE GRADER: POLYSUM

import math
def polysum (n, s):
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    perimeter = n*s
    sum = area + perimeter**2
    return round(sum,4)
