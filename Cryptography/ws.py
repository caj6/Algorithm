def merse(v):
    l = [];
    for i in range(v):
        m = (2**i) - 1;
        l.append(m)
    return l

#------------------------------------------------------------------------------------------

def fer(n):
    if n >= 0:
        F = (2**2**n) + 1
        return F

#-------------------------------------------------------------------------------------------
    