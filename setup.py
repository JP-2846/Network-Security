from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [
                req.strip() for req in requirements if HYPEN_E_DOT != req.strip()
            ]
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="JigarPanchal",
    author_email="JPanchal2305@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
