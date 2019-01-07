import timeit

python_code = timeit.timeit('''py_factorial.py_factorial(50)''',setup='import py_factorial',number=100)
cython_code = timeit.timeit('''factorial.factorial(50)''',setup='import factorial', number=100)

print(cython_code, python_code)
print('Cython is {}x faster'.format(cython_code*100/python_code))
