from ctypes import *

load_c = CDLL("./helloworld.so")

output = load_c.hello("Global Services")
