from setuptools import setup, find_packages

setup(
    name="Topsis-Lav-102203621",  # Name of your package
    version="0.1",  # Package version
    author="Lav Kumar",  # Your name
    author_email="your-email@example.com",  # Your email (optional)
    description="A Python package for TOPSIS method",  # Short description of the package
    long_description=open("README.md").read(),  # Long description from README.md
    long_description_content_type="text/markdown",  # File type for long description
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=["pandas", "numpy"],  # External dependencies
    entry_points={  # Command line tools (optional)
        "console_scripts": [
            "topsis=topsis.topsis:main",  # This allows running the package from the command line using `topsis`
        ],
    },
)

