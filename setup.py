from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        requirements = [req for req in requirements if req and not req.startswith("#")]
        # Remove the "-e ." entry if it exists
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="E2EDSProject",
    version="0.0.1",
    author="Abhijeet Gupta",
    author_email="abhijeetv.2015@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
