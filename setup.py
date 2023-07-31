from setuptools import setup, find_packages

setup(
    name='HW09_Package',
    version='1.0.0',
    url='https://github.com/mtvaden1/DS5100_HW09',
    author='Michael Vaden',
    author_email='mtv2eva@virginia.edu',
    description='Package for M09 Homework',
    license='MIT',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)