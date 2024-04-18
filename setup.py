import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME="Text-Summarizer"
AUTHOR_USER_NAME="67B8"
SRC_REPO="textsummarizer"
AUTHOR_EMAIL="21b81a67b8.cvr@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/67B8/Text-Summarizer",
    project_urls={
        "Bug Tracker": "https://github.com/67B8/Text-Summarizer/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
    
