from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("nebula",  ["nebula.py"]),
]
setup(
    name = 'nebula',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
