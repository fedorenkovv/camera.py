from distutils.core import setup

setup(
    name='Camera',
    version='0.1.0.1',
    py_modules=['camera'],
    license='The MIT License',
    long_description=open('README.rst').read(),
    install_requires=['pyyaml', 'numpy', 'scipy']
)
