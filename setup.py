from setuptools import setup, find_packages

setup(
    name="Topsis-Lav-102203621",
    version="0.1",
    author="Lav Kumar",
    description="A Python package for TOPSIS method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",
        ],
    },
)
