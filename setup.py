from setuptools import setup, find_packages

setup(
    name="quantum_ai_engineering",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "qiskit",
        "cirq",
        "tensorflow",
        "transformers",
        "scikit-learn"
    ],
    author="Mohammed Amine Abdelouareth",
    author_email="your.email@example.com",
    description="AI-Driven Quantum Software Engineering Framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/amineyzu/ai-quantum-engineering",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Quantum Computing"
    ],
    python_requires=">=3.8",
) 