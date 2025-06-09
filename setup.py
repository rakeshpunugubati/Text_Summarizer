import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer"
AUTH_USER_NAME = "rakeshpunugubati"
SRC_REPO ="textSummarizer"
AUTHOR_EMAIL = "rakesh.ponugubati@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTH_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python library for text summarization NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTH_USER_NAME + "/" + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/" + AUTH_USER_NAME + "/" + SRC_REPO + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    
)