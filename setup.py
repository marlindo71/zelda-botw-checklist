# coding=utf-8
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='zelda-botw-checklist',
    version='0.1',
    description="Zelda BOTW Checklist is a python program tha generates quests checklist of"
                "Zelda Breath of The Wild game from savegame file",
    long_description=readme,
    packages=find_packages(),
    url='https://github.com/marlindo71/zelda-botw-checklist',
    download_url='https://github.com/marlindo71/zelda-botw-checklist/archive/0.1.tar.gz',
    license='GPLv3',
    author='Marlon Andrade',
    author_email='marlindo71@gmail.com',
    keywords=['zelda', 'botw', 'excel', 'checklist', 'savegame'],
    entry_points={
        'console_scripts': [
            'zelda-botw-checklist=zelda-botw-checklist.__main__:main'
        ]
    },
    include_package_data=True,
    install_requires=[
        'click',
        'openpyxl'
    ],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7.7',
    ],
)
