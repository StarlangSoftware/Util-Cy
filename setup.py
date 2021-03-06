from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["Util/*.pyx", "Util/*.pxd"], compiler_directives={'language_level' : "3"}),
    name='NlpToolkit-Util-Cy',
    version='1.0.3',
    packages=['Util'],
    package_data={'Util': ['*.pxd', '*.pyx', '*.c']},
    url='https://github.com/StarlangSoftware/Util-Cy',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Simple Utils'
)
