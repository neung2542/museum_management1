from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in museum_management/__init__.py
from museum_management import __version__ as version

setup(
	name="museum_management",
	version=version,
	description="museum management system",
	author="tyler",
	author_email="thehasaki123@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
