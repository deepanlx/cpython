cdef extern from "helloworld.c":
    void hello(char str[20])

def my_bridge_function():
    return hello("Cdef GS")
