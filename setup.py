from distutils.core import setup

from setuptools import find_packages

setup(
	name='mssh',
	version='0.1',
	packages=find_packages(),
	url='https://github.com/foofilers/mssh2',
	license='GPLv3',
	author='Igor Maculan',
	author_email='n3wtron@gmail.com',
	description='ssh manager',
	requires=['PyYAML'],
	scripts=['bin/mssh']
)
