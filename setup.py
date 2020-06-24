import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='blaze-distributions',
    version='0.2',
    author= 'Toluwalope Oluyipe',
    author_email= 'kingtoluwalope@gmail.com',
    description="A Binomial and Gaussian Distribution Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)