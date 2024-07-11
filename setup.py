from setuptools import find_packages, setup

packages = [
    "requests==2.27.*",
    "requests-mock==1.9.*",
    "pytest==7.*",
    "pytest-cov",
    "pytest-timeout",
]

setup(
    name="oop-rest-client-easy",
    version="1.0.0",
    author="Devskiller.com",
    author_email="support@devskiller.com",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    setup_requires=["pytest-runner"],
    tests_require=packages,
)
