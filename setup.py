from setuptools import setup, find_packages

setup(
    name="mStock-TradingApi-B",
    version="0.1.1",
    author="Mirae Asset Capital Markets Ltd.",
    description="A Python SDK for Connecting to mStock Trading API and Streaming API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MiraeAsset-mStock/pytradingapi-typeB",
    packages=find_packages(include=["tradingapi_b", "tradingapi_b.*"]),
    package_dir={"tradingapi_b": "tradingapi_b"},
    install_requires=[
        "autobahn", 
        "requests",
        "responses",
        "pytest",
        "setuptools",
        "twisted"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires=">=3.11",
)