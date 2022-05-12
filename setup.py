import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toyproblems", # Replace with your own username
    version="0.0.1",
    author="John Park",
    author_email="parkjohnyc@gmail.com",
    description="Toy Problem data and code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnypark/ToyProblems",
    packages=setuptools.find_packages(),
    install_requires = ['tensorflow'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

