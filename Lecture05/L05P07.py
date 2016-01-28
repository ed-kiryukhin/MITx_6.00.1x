# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/videosequence:Lecture_5/

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == "":
        return 0
    else:
        return 1 + lenRecur(aStr[0:-1])
