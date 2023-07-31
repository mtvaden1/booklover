from setuptools import setup, find_packages

setup(
    name='booklover',
    version='1.0.0',
    url='https://github.com/mtvaden1/booklover',
    author='Michael Vaden',
    author_email='mtv2eva@virginia.edu',
    description='Package for M09 Homework',
    license='MIT',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)