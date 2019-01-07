def py_factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*py_factorial(n-1))
