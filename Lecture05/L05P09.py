# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/videosequence:Lecture_5/

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False
    if str1 == str2:
        return True
    else:
        return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])
