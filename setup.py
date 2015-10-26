from setuptools import setup, find_packages

setup(name='SplitTests',
      entry_points={
          'nose.plugins.0.10': [
              'splittests=SplitTests'
          ]
      },
      packages=find_packages(),
      install_requires=['nose'],
      version="0.0.1",
      author='yellowbeard',
      author_email='lee@bonafide.co',
      url='https://github.com/numeratechoir/laserlike',
      )

