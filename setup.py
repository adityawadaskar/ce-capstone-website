from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy'
]

setup(
    name='ce-capstone',
    version='0.0',
    description='CE Capstone Website',
    author='Aditya Wadaskar',
    author_email='wadaskar.aditya@gmail.com',
    keywords='web flask capstone ce',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)