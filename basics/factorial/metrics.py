from py_factorial import py_factorial
from factorial import factorial
import time

start = time.time()
py_factorial(50)
end = time.time()
result = end - start

print(result)

start = time.time()
factorial(50)
end = time.time()
result = end - start
print(result)
