from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    requirements = []
    
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ i.replace("\n", "") for i in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        

setup(name = "MlProject",
      version="0.0.1",
      description="Machine Learning Pipeline Project",
      author="Prashant Kokande",
      author_email="prashant.kokande99@gmail.com",
      packages = find_packages(),
      install_requires = get_requirements("requirements.txt")
    )