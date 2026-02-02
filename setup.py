from setuptools import setup, find_packages

HYPEN_ELLIPSE = '-e .'
def get_requirements():
    with open('requirements.txt') as f:
        req = f.read().splitlines()
        if HYPEN_ELLIPSE in req:
            req.remove(HYPEN_ELLIPSE)
        return req
        
setup(
    name="mlproject",
    version="0.0.1",
    author="Karan",
    author_email="karanshrivastava00@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
