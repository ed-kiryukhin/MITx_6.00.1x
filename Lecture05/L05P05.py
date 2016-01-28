# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/videosequence:Lecture_5/

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if min(a, b) == 0:
        return max(a, b)
    else:
        return gcdRecur(min(a, b), max(a, b) % min(a, b)) 
