"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "pybusinesscentral"
VERSION = "2.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="(v2.0) Dynamics 365 Business Central",
    author="Uptick",
    author_email="support@uptickhq.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "(v2.0) Dynamics 365 Business Central"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    (v2.0) Business Central Standard APIs  # noqa: E501
    """
)
