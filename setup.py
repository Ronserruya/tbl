from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tbl',
    version='0.0.1',
    author="Ron Serruya",
    author_email="ron.serruya@gmail.com",
    description="csv files printer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ronserruya/tbl",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['rapidtables==0.1.7', 'click==7'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points='''
    [console_scripts]
    tbl=tbl.cli:main
    ''',
    python_requires='>=3.4',
)
