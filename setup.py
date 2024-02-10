import re

from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
  requirements = []
  with open(file_path) as file:
    requirements = file.readlines()
    requirements = [re.sub('\n', '', req) for req in requirements]    
  return requirements

setup(
  name='Trainer Application for Duplicated Bug Report Detection',
  version='0.1',
  author='Reza Dzikri',
  author_email='rezadzikri@gmail.com',
  description='Model trainer application for duplicated bug report detection design with scalable and maintainable clean architecture.',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt'),
  license='MIT',
  python_requires='>=3.10'
)