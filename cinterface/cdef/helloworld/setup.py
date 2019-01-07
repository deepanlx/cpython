from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles = ['cython_helloworld.pyx']
ext_modules = [Extension("cython_hello", 
                          sourcefiles
                          )]

setup(
  name = 'cython_hello_extern',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
