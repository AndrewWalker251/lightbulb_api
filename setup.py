from setuptools import setup
from setuptools import find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
        REQUIRED = f.read().split("\n")
except:
    REQUIRED = []

setup(name='image_classifier',
      version='0.1.0',
      description='bulb classifier',
      author='Andrew Walker',
      author_email='andrewjwalker251@gmail.com',
      url='https://github.com/AndrewWalker251/lightbulb_app.git',
      install_requires=REQUIRED,
      packages=find_packages(exclude=("example", "app", "data", "docker", "tests")))

