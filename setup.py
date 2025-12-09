from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    ''' this fn return 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        


setup(
    name="mlbpmk",
    version="0.0.1",
    author="Mukesh",
    author_email="mukesh.cs130@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    entry_points={
        "console_scripts": [
            "mypkg=mypackage.main:main",
        ]
    }
)




# setup(
#     name="mlbpmk",
#     version="0.0.1",
#     author="Mukesh",
#     author_email="mukesh.cs130@gmail.com",
#     packages=find_packages(),
#     install_requires=['pandas','numpy','seaborn'],
#     entry_points={
#         "console_scripts": [
#             "mypkg=mypackage.main:main",
#         ]
#     }
# )
