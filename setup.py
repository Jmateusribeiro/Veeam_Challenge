from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='veeam_challenge',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'challenge = chalenge.main:main',
        ],
    },
    author='Jorge Ribeiro',
    author_email='mateusribeirojorge@gmail.com',
    description='Veeam Challenge - Folder Synchronization',
    url='https://github.com/Jmateusribeiro/Veeam_Challenge',
)