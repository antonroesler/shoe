from setuptools import setup
setup(
    name='shoe',
    version='0.1.0',
    packages=['shoe'],
    entry_points={
        'console_scripts': [
            'shoe = shoe.__main__:main'
        ]
    })