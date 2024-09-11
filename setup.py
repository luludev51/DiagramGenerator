from setuptools import setup, find_packages

setup(
    name="diagramme",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[matplotlib.pyplot, io, base64],  # Mets ici les dépendances nécessaires
    author="luludev51",
    author_email="luludev511@gmail.com",
    description="A library for creating charts in Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
