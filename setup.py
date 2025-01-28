from setuptools import setup

setup(
    name='valorant-stretched',
    version='0.1',
    packages=['valorant_stretched'],
    entry_points={
        'console_scripts': [
            'vstretched = valorant_stretched.__init__:main',
        ],
    },
    install_requires=[
        'configparser',  # Ensure configparser is available for Python 2.x compatibility
    ],
)