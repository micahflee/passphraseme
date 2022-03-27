import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="passphraseme",
    version="0.1.5",
    author="Micah Lee",
    author_email="micah@micahflee.com",
    description="A quick and simple cryptographically secure script to generate high entropy passphrases using the Electronic Frontier Foundation's wordlists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3+",
    url="https://github.com/micahflee/passphraseme",
    packages=["passphraseme"],
    package_data={"passphraseme": ["wordlists/*.txt"]},
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Intended Audience :: System Administrators",
    ),
    entry_points={
        "console_scripts": [
            "passphraseme = passphraseme:main",
        ],
    },
)
