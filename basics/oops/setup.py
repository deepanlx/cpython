from distutils.core import setup
from Cython.Build import cythonize

setup(name='sftp',
      ext_modules=cythonize("sftp.pyx"))
