from setuptools import setup, find_packages

setup(name="pysimpletcp",
        version="1.0.0",
        description="Simple TCP server and client implementation in Python",
        author="Kristof Floch",
        packages=find_packages(),
        install_requires=["pyyaml"])