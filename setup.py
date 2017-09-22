from setuptools import setup, find_packages

setup(name='hacky',

      version='0.1',

      url='https://github.com/pytorn/hacky',

      license='Apache 2.0',

      author='Ashwini Purohit',

      author_email='geek.ashwini@gmail.com',

      description='A unicorn for Hackathons',

      packages=find_packages(exclude=['tests']),

      long_description=open('README.md').read(),

      zip_safe=False,

      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2.7',
      ],

      setup_requires=[])
