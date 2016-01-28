# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/videosequence:Lecture_5/

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max_divisor = 1
    for divisor in range(2, min(a, b) + 1):
        if a % divisor == 0 and b % divisor == 0:
            max_divisor = divisor
    return max_divisor
