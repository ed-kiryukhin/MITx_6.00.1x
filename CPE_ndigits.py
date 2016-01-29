def ndigits(x):
    '''
    x: integer, either positive or negative
    returns: integer, the number of digits in x
    
    base case: if x from 0 to 9, returns 1
    recursive case: otherwise return 1 + ndigits(x / 10)
    '''
    if abs(x) < 10:
        return 1
    else:
        return 1 + ndigits(x / 10)
