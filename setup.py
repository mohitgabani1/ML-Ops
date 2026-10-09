from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="mlops_project", # like keras, sklearn
    version="0.1.0",
    author='Mohit',
    author_email='mohitgabani1@gmail.com',
    description="A machine learning project with MLOps practices",
    packages=find_packages(where="src"), # tells setuptools to look for packages in the src directory
    # it creates like mlops_project.components, mlops_project.pipeline
    package_dir={"": "src"}, # root directory for packages is src
    url="https://github.com/mohitgabani1/ML-Ops.git", # meta data
    install_requires=get_requirements("requirements_dev.txt") # install dependencies from requirements_dev.txt
)