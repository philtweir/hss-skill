import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hss_skill",
    version="0.1.2",
    author="Patrick Fial",
    author_email="mg.m@gmx.net",
    description="Library for creating voice assistant skills for the hermes skill server (hss-server)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patrickjane/hss-skill",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'rpyc',
    ],
    python_requires='>=3.6',
)
