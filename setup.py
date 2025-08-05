"""
Setup script for pyzatca package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyzatca",
    version="1.0.0",
    author="Python ZATCA Community",
    author_email="support@example.com",
    description="ZATCA (Fatoora) QR-Code Implementation for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/pyzatca",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial :: Accounting",
    ],
    python_requires=">=3.7",
    install_requires=[
        "cryptography>=3.4.8",
        "qrcode[pil]>=7.3.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.10",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    keywords="zatca, e-invoicing, qr-code, saudi-arabia, fatoora, arabic",
    project_urls={
        "Bug Reports": "https://github.com/example/pyzatca/issues",
        "Source": "https://github.com/example/pyzatca",
        "Documentation": "https://github.com/example/pyzatca#readme",
    },
    include_package_data=True,
    zip_safe=False,
) 