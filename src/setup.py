import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    version="0.0.1",
    author="Lucas Staudt",
    author_email="lucas.std1@gmail.com",
    description="Sample of Selenium project with SeleniumBase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.0.*',
)
