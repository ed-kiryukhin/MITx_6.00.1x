
# https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/sp13_Problem_Set_3/

# RADIATION EXPOSURE

'''
Computes and returns the amount of radiation exposed
to between the start and stop times. Calls the 
function f (defined for you in the grading script)
to obtain the value of the function at any point.

start: integer, the time at which exposure begins (not for recursive method)
stop: integer, the time at which exposure ends (not for recursive method)
step: float, the width of each rectangle. You can assume that
the step size will always partition the space evenly.

returns: float, the amount of radiation exposed to 
between start and stop times.
'''

def radiationExposureIter(start, stop, step):
    amount_rad = 0
    for i in xrange(0, int((stop - start) / step)):
        amount_rad += f(start + step * i) * step
    return amount_rad

def radiationExposureRec(start, stop, step):
    if (stop - start - step) < 0.0001:
        return f(start) * step
    else:
        return f(start) * step + radiationExposureRec(start + step, stop, step)
