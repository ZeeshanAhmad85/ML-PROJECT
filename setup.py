from setuptools import setup,find_packages
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(filename: str) -> List[str]:
    """Get the requirements from requirements.txt"""
    requirements = []
    with open(filename) as f:
       requirements = f.readlines()
       requirements=[req.replace('\n',"") for req in requirements]
       if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='ML_PROJECT',
    version='0.0.1',
   # description='SSD: Single Shot MultiBox Detector, in PyTorch',
    author='Zeeshan Ahmed',
    author_email="zeeshan6842895@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
    

