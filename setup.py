import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Denzven-Graphing-Api-Wrapper",
    version="0.0.0.3",
    author="Denzven",
    author_email="denzvenvadakkan@gmail.com",
    description="An Api Wrapper for the Denzven-Graphing-Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/denzven/Denzven-Graphing-Api-Wrapper",
    project_urls={
	"Bug Tracker": "https://github.com/denzven/Denzven-Graphing-Api-Wrapper/issues",
	"Documentation": "https://denzgraphingapiwrapper-py.readthedocs.io/en/latest/",
	"Source": "https://github.com/denzven/Denzven-Graphing-Api-Wrapper"

    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)