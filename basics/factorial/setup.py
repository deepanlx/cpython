from distutils.core import setup
from Cython.Build import cythonize

setup(name='factorial',
      ext_modules=cythonize("factorial.pyx"))
