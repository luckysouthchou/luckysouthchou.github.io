def xingnan(n):
    if n == 0:
        return 0
    elif n == 9:
        return
    else:
        return xingnan(n-1) + xingnan(n-2)
