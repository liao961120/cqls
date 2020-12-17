from setuptools import setup

with open("README.md", encoding="utf-8") as f:
      long_description = f.read().strip()

setup(name='cqls',
      version='0.1.5',
      description='A parser for an often-used subset of Corpus Query Language',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/liao961120/cqls',
      author='Yongfu Liao',
      author_email='liao961120@github.com',
      license='MIT',
      packages=['cqls'],
      tests_require=['deepdiff'],
      zip_safe=False)
