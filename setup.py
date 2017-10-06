from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='hackr',

      version='0.1.2',

      url='https://github.com/pytorn/hackr',

      license='Apache 2.0',

      author='Ashwini Purohit',

      author_email='geek.ashwini@gmail.com',

      description='A unicorn for Hackathons',

      packages=find_packages(exclude=['tests']),

      long_description=open('README.rst').read(),

      zip_safe=False,

      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
      ],

      install_requires=required,

      setup_requires=[])
