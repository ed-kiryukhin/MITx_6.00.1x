https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/videosequence:Lecture_5/

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    if len(aStr) == 1 and aStr != char:
        return False
    elif aStr[int(round(len(aStr) / 2))] == char:
        return True
    else:
        if aStr[int(round(len(aStr) / 2))] > char:
            return isIn(char, aStr[:int(round(len(aStr) / 2))])
        elif aStr[int(round(len(aStr) / 2))] < char:
            return isIn(char, aStr[int(round(len(aStr) / 2)):])
