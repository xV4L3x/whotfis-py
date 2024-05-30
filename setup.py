from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = "Simple package to interact with the whois command line tool"

setup(
    name="whotfis-py",
    version=VERSION,
    author="Valerio Pio De Nicola",
    author_email="valeriopio02@gmail.com",
    description=DESCRIPTION,
    long_description=open('whotfis-py/README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'whois', 'whois command line', 'whois python', 'whois python package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ],
)