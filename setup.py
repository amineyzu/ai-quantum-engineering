from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-quantum-engineering",
    version="0.1.0",
    author="Mohammed Amine Abdelouareth",
    author_email="chinajiyanxin@gmail.com",
    description="An open-source framework for AI-driven quantum software engineering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amineyzu/ai-quantum-engineering",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "qiskit>=0.34.0",
        "tensorflow>=2.8.0",
        "transformers>=4.20.0",
        "pytest>=7.0.0",
    ],
) 